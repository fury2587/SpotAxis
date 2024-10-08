# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-11 19:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0020_auto_20170802_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalReferal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='companies.Company')),
            ],
            options={
                'verbose_name': 'External Referal',
                'verbose_name_plural': 'External Referals',
            },
        ),
    ]
