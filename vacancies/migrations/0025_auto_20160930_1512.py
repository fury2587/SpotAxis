# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-30 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0024_auto_20160929_1837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('logtime', 'stage'), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
