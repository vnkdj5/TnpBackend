# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-24 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_company_code_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='be_college_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='be_or_me',
            field=models.CharField(blank=True, default='BE', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='be_passing_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='be_university',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='be_yeargap_reason',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='me_firt_year_marks',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
