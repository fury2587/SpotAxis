# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-08 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0030_auto_20161007_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='ban_period',
            field=models.CharField(blank=True, choices=[[b'1', b'1 month'], [b'2', b'2 months'], [b'3', b'3 months'], [b'4', b'4 months'], [b'5', b'5 months'], [b'6', b'6 months'], [b'7', b'7 months'], [b'8', b'8 months'], [b'9', b'9 months'], [b'10', b'10 months'], [b'11', b'11 months']], default=None, max_length=2, null=True),
        ),
    ]
