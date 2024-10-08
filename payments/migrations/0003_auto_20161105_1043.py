# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-05 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20161105_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'ordering': ('-timestamp',), 'verbose_name': 'Transaction', 'verbose_name_plural': 'Transactions'},
        ),
        migrations.AlterUniqueTogether(
            name='priceslab',
            unique_together=set([('currency', 'slab_period', 'package')]),
        ),
    ]
