# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 23:18
from __future__ import unicode_literals

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import vacancies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_Fav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Add Date')),
                ('candidate', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate', verbose_name='Candidate')),
            ],
            options={
                'ordering': ('-vacancy', '-add_date'),
                'verbose_name': 'Favourite Vacancy',
                'verbose_name_plural': 'Favourite Vacancies',
            },
        ),
        migrations.CreateModel(
            name='Employment_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Name')),
                ('codename', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('order', models.PositiveSmallIntegerField(blank=True, default=100, null=True)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Employment Experience',
                'verbose_name_plural': 'Employment Experiences',
            },
        ),
        migrations.CreateModel(
            name='Postulate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False, verbose_name='Seen')),
                ('discard', models.BooleanField(default=False, verbose_name='Discarded')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Add Date')),
                ('candidate', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate', verbose_name='Candidate')),
            ],
            options={
                'ordering': ('-vacancy', '-add_date', '-seen'),
                'verbose_name': 'Application',
                'verbose_name_plural': 'Aplications',
            },
        ),
        migrations.CreateModel(
            name='PubDate_Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Name')),
                ('days', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Days')),
                ('codename', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
            options={
                'ordering': ['days'],
                'verbose_name': 'Day for Search',
                'verbose_name_plural': 'Days for search',
            },
        ),
        migrations.CreateModel(
            name='Public_Postulate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Full Name')),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='E-mail')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Age')),
                ('salary', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Salary')),
                ('description', models.TextField(blank=True, default=None, max_length=50, null=True, verbose_name='Description')),
                ('file', models.FileField(blank=True, null=True, upload_to=vacancies.models.public_path)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Add Date')),
            ],
            options={
                'ordering': ('-vacancy', '-add_date'),
                'verbose_name': 'Public Application',
                'verbose_name_plural': 'Public Applications',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Question')),
                ('answer', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Answer')),
                ('question_date', models.DateTimeField(auto_now_add=True, verbose_name='Question date')),
                ('answer_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Answer Date')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ('-question_date',),
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Salary_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Name')),
                ('codename', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('order', models.PositiveSmallIntegerField(blank=True, default=100, null=True)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Type of Salary',
                'verbose_name_plural': 'Types of Salaries',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment', models.CharField(blank=True, default=None, max_length=70, null=True, verbose_name='Post')),
                ('description', ckeditor.fields.RichTextField(blank=True, default=None, null=True, verbose_name='Description of Post')),
                ('min_age', models.CharField(blank=True, choices=[(0, 'Indistinct'), [b'18', b'18'], [b'19', b'19'], [b'20', b'20'], [b'21', b'21'], [b'22', b'22'], [b'23', b'23'], [b'24', b'24'], [b'25', b'25'], [b'26', b'26'], [b'27', b'27'], [b'28', b'28'], [b'29', b'29'], [b'30', b'30'], [b'31', b'31'], [b'32', b'32'], [b'33', b'33'], [b'34', b'34'], [b'35', b'35'], [b'36', b'36'], [b'37', b'37'], [b'38', b'38'], [b'39', b'39'], [b'40', b'40'], [b'41', b'41'], [b'42', b'42'], [b'43', b'43'], [b'44', b'44'], [b'45', b'45'], [b'46', b'46'], [b'47', b'47'], [b'48', b'48'], [b'49', b'49'], [b'50', b'50'], [b'51', b'51'], [b'52', b'52'], [b'53', b'53'], [b'54', b'54'], [b'55', b'55'], [b'56', b'56'], [b'57', b'57'], [b'58', b'58'], [b'59', b'59'], [b'60', b'60'], [b'61', b'61'], [b'62', b'62'], [b'63', b'63'], [b'64', b'64'], [b'65', b'65']], default=None, max_length=2, null=True)),
                ('max_age', models.CharField(blank=True, choices=[(0, 'Indistinct'), [b'18', b'18'], [b'19', b'19'], [b'20', b'20'], [b'21', b'21'], [b'22', b'22'], [b'23', b'23'], [b'24', b'24'], [b'25', b'25'], [b'26', b'26'], [b'27', b'27'], [b'28', b'28'], [b'29', b'29'], [b'30', b'30'], [b'31', b'31'], [b'32', b'32'], [b'33', b'33'], [b'34', b'34'], [b'35', b'35'], [b'36', b'36'], [b'37', b'37'], [b'38', b'38'], [b'39', b'39'], [b'40', b'40'], [b'41', b'41'], [b'42', b'42'], [b'43', b'43'], [b'44', b'44'], [b'45', b'45'], [b'46', b'46'], [b'47', b'47'], [b'48', b'48'], [b'49', b'49'], [b'50', b'50'], [b'51', b'51'], [b'52', b'52'], [b'53', b'53'], [b'54', b'54'], [b'55', b'55'], [b'56', b'56'], [b'57', b'57'], [b'58', b'58'], [b'59', b'59'], [b'60', b'60'], [b'61', b'61'], [b'62', b'62'], [b'63', b'63'], [b'64', b'64'], [b'65', b'65']], default=None, max_length=2, null=True)),
                ('min_salary', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Minimum Salary')),
                ('max_salary', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Maximum Salary')),
                ('seen', models.IntegerField(blank=True, default=0, null=True, verbose_name='Seen')),
                ('postulate', models.BooleanField(default=True, verbose_name='Applications allowed?')),
                ('applications', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Number of applications')),
                ('confidential', models.BooleanField(default=False, verbose_name='Confidential?')),
                ('data_contact', models.BooleanField(default=True, verbose_name='Contact data?')),
                ('another_email', models.BooleanField(default=False, verbose_name='Send nominatins to another email')),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='E-mail')),
                ('pub_after', models.BooleanField(default=False, verbose_name='Post on a future date?')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Add Date')),
                ('pub_date', models.DateField(default=datetime.date.today, verbose_name='Date of publication')),
                ('editing_date', models.DateField(verbose_name='Editing Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('questions', models.BooleanField(default=True, verbose_name='Allow questions?')),
                ('hiring_date', models.DateField(blank=True, null=True, verbose_name='Date of Joining')),
                ('vacancies_number', models.PositiveSmallIntegerField(blank=True, default=1, null=True, verbose_name='Number of Vacancies')),
                ('public_cvs', models.BooleanField(default=False, verbose_name='Allow public CV?')),
                ('area', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Area', verbose_name='Area')),
                ('company', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.Company', verbose_name='Company')),
                ('degree', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Degree', verbose_name='Degree')),
                ('employmentExperience', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacancies.Employment_Experience', verbose_name='Experience')),
                ('employmentType', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Employment_Type', verbose_name='Type of employment')),
                ('gender', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Gender', verbose_name='Gender')),
                ('industry', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Industry', verbose_name='Industry')),
                ('municipal', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Municipal', verbose_name='City')),
                ('salaryType', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacancies.Salary_Type', verbose_name='Type of Salary')),
                ('state', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.State', verbose_name='State')),
            ],
            options={
                'ordering': ('-pub_date', '-id'),
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
            },
        ),
        migrations.CreateModel(
            name='Vacancy_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=vacancies.models.upload_files_to_vacancy_path)),
                ('random_number', models.IntegerField(blank=True, default=None, null=True, verbose_name=b'Identificador')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de alta')),
                ('vacancy', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.Vacancy', verbose_name=b'Vacancy')),
            ],
            options={
                'ordering': ('-vacancy', '-add_date', 'random_number'),
                'verbose_name': 'Archivos Adjuntos a Vacancy',
                'verbose_name_plural': 'Archivos Adjuntos a Vacancies',
            },
        ),
        migrations.CreateModel(
            name='Vacancy_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Name')),
                ('codename', models.CharField(blank=True, default=None, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Vacancy Status',
                'verbose_name_plural': 'Vacancy Statuses',
            },
        ),
        migrations.AddField(
            model_name='vacancy',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vacancies.Vacancy_Status', verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='question',
            name='vacancy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.Vacancy', verbose_name='Vacancy'),
        ),
        migrations.AddField(
            model_name='public_postulate',
            name='vacancy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.Vacancy', verbose_name='Vacancy'),
        ),
        migrations.AddField(
            model_name='postulate',
            name='vacancy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vacancies.Vacancy', verbose_name='Vacancy'),
        ),
        migrations.AddField(
            model_name='candidate_fav',
            name='vacancy',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='vacancies.Vacancy', verbose_name='Vacancy'),
        ),
    ]
