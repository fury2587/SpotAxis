# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-01 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0011_subscription_auto_renew'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='services',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
