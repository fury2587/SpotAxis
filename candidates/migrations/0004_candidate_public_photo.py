# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-03 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_auto_20160824_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='public_photo',
            field=models.ImageField(blank=True, default=None, max_length=200, null=True, upload_to=b'photos/', verbose_name='Photo'),
        ),
    ]
