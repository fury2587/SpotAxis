# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-28 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_auto_20160928_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiterinvitation',
            name='application_process_management',
        ),
        migrations.RemoveField(
            model_name='recruiterinvitation',
            name='job_management',
        ),
        migrations.RemoveField(
            model_name='recruiterinvitation',
            name='site_management',
        ),
        migrations.RemoveField(
            model_name='recruiterinvitation',
            name='team_management',
        ),
        migrations.AddField(
            model_name='recruiterinvitation',
            name='membership',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
