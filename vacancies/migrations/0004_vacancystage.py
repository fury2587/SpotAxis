# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-16 11:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_stage'),
        ('candidates', '0001_initial'),
        ('vacancies', '0003_auto_20160815_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Order')),
                ('locked', models.BooleanField(default=False, verbose_name='Locked')),
                ('candidates', models.ManyToManyField(default=None, to='candidates.Candidate', verbose_name='Candidate')),
                ('stage', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.Stage', verbose_name='Stage Name')),
                ('vacancy', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacancies.Vacancy', verbose_name='Vacancy')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Vacancy Stage',
                'verbose_name_plural': 'Vacancy Stages',
            },
        ),
    ]
