# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-22 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='offset',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='scheduled_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Scheduled On'),
        ),
    ]
