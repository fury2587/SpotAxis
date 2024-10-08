    # -*- coding: utf-8 -*-
from datetime import datetime
from common.models import Currency
from companies.models import Company
from django.db import models
from django.db.models.expressions import Value
from django.db.models.fields import BooleanField
from django.utils.translation import ugettext as _
from TRM import settings
class Active(models.Manager):
    use_for_related_fields = True
    def get_queryset(self):
        return super(Active, self).get_queryset().filter(enabled=True)

class ServiceCategory(models.Model):
    name = models.CharField(null=True, blank=True, default=None, max_length=50)
    codename = models.CharField(null=True, blank=True, default=None, max_length=5)
    enabled = models.BooleanField(default=True, blank = True)

    objects = Active()
    all_objects = models.Manager()

    class Meta:
        verbose_name = "ServiceCategory"
        verbose_name_plural = "ServiceCategories"

    def __str__(self):
        return self.name
 
class Services(models.Model):
    name = models.CharField(verbose_name=_(u'Name of Service'), max_length=100, null=True, blank=True, default=None)
    codename = models.CharField(verbose_name=_(u'Codename'), max_length=30, null=True, blank=True, default=None)
    category = models.ForeignKey(ServiceCategory, null=True, blank=True, default=None)
    enabled = models.BooleanField(default=True, blank = True)
    # cost = models.DecimalField(verbose_name=_(u'Cost for Service'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    # iva = models.DecimalField(verbose_name=_(u'IVA'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    # total = models.DecimalField(verbose_name=_(u'Total'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    # wallet_amount = models.DecimalField(verbose_name=_(u'Total'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    # order = models.PositiveSmallIntegerField(null=True, blank=True, default=None)

    objects = Active()
    all_objects = models.Manager()
    
    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = _(u'Service')
        verbose_name_plural = _(u'Services')
        ordering = ('name',)

class Package(models.Model):
    name = models.CharField(null=True, blank=True, default=None, max_length=50)
    services = models.ManyToManyField(Services)
    free_users = models.PositiveIntegerField(null=True, blank=True, default=0)
    max_users = models.PositiveIntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name = "Package"
        verbose_name_plural = "Packages"

    def __unicode__(self):
        return self.name

    def package_slabs(self):
        currencies = self.priceslab_set.all().values_list('currency').distinct()
        slabset = []
        for currency in currencies:
            if currency[0]:
                slabobject = {'currency':Currency.objects.get(id = currency[0])}
            else:
                slabobject = {'currency': None}
            slabobject['price_slabs'] = self.priceslab_set.all().filter(currency = slabobject['currency'])
            slabobject['ids'] = [sc['category'] for sc in self.services.all().values('category').distinct()]
            slabobject['service_categories'] = ServiceCategory.objects.filter(id__in=slabobject['ids']).annotate(full_package=Value(False, output_field = BooleanField()))
            # print slabobject['service_categories']
            for category in slabobject['service_categories']:
                ids = [c.id for c in category.services_set.all()]
                if set(ids).issubset(set([service.id for service in self.services.all()])):
                    category.full_package = True
            slabobject['service_categories'].order_by('full_package')
            # print slabobject['service_categories'].order_by('full_package')
            slabset.append(slabobject)
        return slabset

    def currencies(self):
        return self.priceslab_set.all().values_list('currency').distinct()
    

SLAB_PERIOD = (
    ('M', _(u'Monthly')),
    ('Y', _(u'Yearly'))
)

class PriceSlab(models.Model):
    currency = models.ForeignKey(Currency, null=True, blank=True, default=None)
    slab_period = models.CharField(choices = SLAB_PERIOD, max_length = 1, null=True, blank=True, default=None)
    expiry_period = models.PositiveSmallIntegerField(null=True, blank=True, default =0)
    amount = models.DecimalField(verbose_name=_(u'Amount'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    buffered_amount = models.DecimalField(verbose_name=_(u'Buffered Amount'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    price_per_user = models.DecimalField(verbose_name=_(u'Price Per User'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    buffered_price_per_user = models.DecimalField(verbose_name=_(u'Buffered Price Per User'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    package = models.ForeignKey(Package, null=True, blank=True, default=None)

    class Meta:
        verbose_name = "Price Slab"
        verbose_name_plural = "Price Slabs"
        unique_together = ('currency', 'slab_period', 'package')

    def __unicode__(self):
        if not self.get_slab_period_display():
            return self.package.name
        else:
            return "%s - %s" % (str(self.package.name), str(self.get_slab_period_display()))
    
    def allows_additional_users(self):
        if self.package.max_users == 0 or self.package.max_users > self.package.free_users:
            return True
        return False

class Subscription(models.Model):
    company = models.OneToOneField(Company, null=True, blank=True, default=None)
    expiry = models.DateTimeField(null=True, blank=True, default=None)
    added_users = models.PositiveIntegerField(null=True, blank=True, default=0)
    price_slab = models.ForeignKey(PriceSlab, null=True, blank=True, default=None)
    auto_renew = models.BooleanField(default = True, blank=True)
    last_week = models.BooleanField(default=False, blank=True)
    last_day = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"

    def __unicode__(self):
        return str(self.expiry)

    def expired(self):
        if self.expiry and self.expiry > datetime.now() or not self.expiry:
            return False
        else:
            return True

    def ends_in(self):
        if self.expiry:
            return self.expiry - datetime.now() 
        else:
            return 0

    def bill_amount(self):
        amount = self.price_slab.amount
        if not amount:
            amount = 0
        if self.added_users:
            amount = amount + (self.added_users*self.price_slab.price_per_user)
        return amount
    
WALLET_MOVEMENTS_TYPE = (
    ('A', _(u'Added')),
    ('R', _(u'Paid'))
)

class Transactions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), null=True, blank=True, default=None, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, verbose_name=_('Company'), null=True, blank=True, default=None, on_delete=models.SET_NULL)
    # service = models.ForeignKey(Services, verbose_name=_('Service'), null=True, blank=True, default=None, on_delete=models.SET_NULL)
    type = models.CharField(verbose_name=_(u'Type of Movement'), choices=WALLET_MOVEMENTS_TYPE, max_length=1, null=True, blank=True, default=None)
    reason = models.CharField(null=True, blank=True, default=None, max_length=200)
    amount = models.DecimalField(verbose_name=_(u'Amount'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    balance = models.DecimalField(verbose_name=_(u'Balance'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    timestamp = models.DateTimeField(verbose_name=_(u'Date'), auto_now_add=True)

    def __unicode__(self):
        return u'%s' % str(self.amount)

    class Meta:
        verbose_name = _(u'Transaction')
        verbose_name_plural = _(u'Transactions')
        ordering = ('-timestamp',)

DISCOUNT_VALUE_TYPE = (
    ('V', _(u'Value')),
    ('P', _(u'Percent'))
)
DISCOUNT_TRANSACTION_TYPE = (
    ('A', _(u'Add')),
    ('S', _(u'Subtract'))
)

class Discount(models.Model):
    name = models.CharField(null=True, default='', blank=True, max_length=200)
    label = models.CharField(null=True, default='', blank=True, max_length=50, unique= True)
    expiry = models.DateField(default=None, null=True, blank=True)
    type = models.CharField(verbose_name=_(u'Type of Value'), choices=DISCOUNT_VALUE_TYPE, max_length=1, null=True, blank=True, default=None)
    transaction_type = models.CharField(verbose_name=_(u'Type of Movement'), choices=DISCOUNT_TRANSACTION_TYPE, max_length=1, null=True, blank=True, default=None)
    currency = models.ForeignKey(Currency, null=True, blank=True, default=None)
    amount = models.DecimalField(verbose_name=_(u'Amount'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    # min_amount = models.DecimalField(verbose_name=_(u'Amount'), max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    max_usage = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    available_to_signups = models.BooleanField(default = True)
    max_usage_per_company = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    enabled = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    plans = models.ManyToManyField(PriceSlab)
    companies = models.ManyToManyField(Company, through="Discount_Usage")

    def __unicode__(self):
        return u'%s' % str(self.amount)

    class Meta:
        verbose_name = 'Discount'
        verbose_name_plural = 'Discounts'
        ordering = ("enabled",'-expiry')   

class ScheduledTransactions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), null=True, blank=True, default=None, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, verbose_name=_('Company'), null=True, blank=True, default=None, on_delete = models.SET_NULL)
    # amount = models.DecimalField(verbose_name="Amount", max_digits=7, decimal_places=2, null=True, blank=True, default=0.00)
    timestamp = models.DateTimeField(verbose_name='Timestamp', auto_now=True)
    discount = models.ForeignKey(Discount, null=True, blank=True, default=None)
    added_users = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    price_slab = models.ForeignKey(PriceSlab, null=True, blank=True, default=None)

    def __unicode__(self):
        return u'%s' % str(self.company)

    class Meta:
        verbose_name = "Scheduled Transaction"
        verbose_name_plural = "Scheduled Transactions"
        ordering = ("-timestamp",)
   

class Discount_Usage(models.Model):
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    used_count = models.PositiveSmallIntegerField(default=0, null=True, blank=True)

    def __unicode__(self):
        return str(self.company)
    class Meta:
        verbose_name='Discount_Usage'
        verbose_name_plural = 'Discount Usages'
        ordering = ("discount", "timestamp")


### IF YOU ADD ADDITIONAL MODELS, DO NOT FORGET TO REGISTER THEM IN ADMIN ###
