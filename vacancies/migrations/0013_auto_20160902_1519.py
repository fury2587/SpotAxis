# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-02 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0012_auto_20160902_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postulate',
            name='vacancy_stage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.VacancyStage'),
        ),
        migrations.AlterField(
            model_name='public_postulate',
            name='vacancy_stage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.VacancyStage'),
        ),
    ]
