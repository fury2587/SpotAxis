# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-24 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='public_email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='academic',
            name='area',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Specialisation'),
        ),
    ]
