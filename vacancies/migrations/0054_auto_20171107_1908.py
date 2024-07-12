# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-11-07 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0053_postulate_external_referer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Medium',
                'verbose_name_plural': 'Mediums',
            },
        ),
        migrations.AlterField(
            model_name='postulate',
            name='external_referer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='companies.ExternalReferal'),
        ),
        migrations.AddField(
            model_name='postulate',
            name='medium',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='vacancies.Medium'),
        ),
    ]
