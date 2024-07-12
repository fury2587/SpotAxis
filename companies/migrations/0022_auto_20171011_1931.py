# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-11 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0021_externalreferal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externalreferal',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company'),
        ),
    ]
