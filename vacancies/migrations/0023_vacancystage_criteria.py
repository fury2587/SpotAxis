# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-27 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_auto_20160920_1740'),
        ('vacancies', '0022_auto_20160922_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulate',
            name='recruiter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Recruiter'),
        ),
        migrations.AddField(
            model_name='vacancystage',
            name='recruiters',
            field=models.ManyToManyField(default=None, to='companies.Recruiter'),
        ),
        migrations.AddField(
            model_name='stagecriterion',
            name='vacancy_stage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.VacancyStage', verbose_name=b'Vacancy Stage'),
        ),
        migrations.AddField(
            model_name='public_postulate_stage',
            name='postulate',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.Postulate', verbose_name=b'Postulate Stage'),
        ),
        migrations.AddField(
            model_name='public_postulate_stage',
            name='scores',
            field=models.ManyToManyField(default=None, to='vacancies.Postulate_Score'),
        ),
        migrations.AddField(
            model_name='public_postulate_stage',
            name='vacancy_stage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.VacancyStage', verbose_name=b'Vacancy Stage'),
        ),
        migrations.AddField(
            model_name='postulate_stage',
            name='postulate',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.Postulate', verbose_name=b'Postulate Stage'),
        ),
        migrations.AddField(
            model_name='postulate_stage',
            name='scores',
            field=models.ManyToManyField(default=None, to='vacancies.Postulate_Score'),
        ),
        migrations.AddField(
            model_name='postulate_stage',
            name='vacancy_stage',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.VacancyStage', verbose_name=b'Vacancy Stage'),
        ),
    ]
