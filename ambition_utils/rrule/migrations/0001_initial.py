# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 17:08
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rrule_params', django.contrib.postgres.fields.jsonb.JSONField()),
                ('meta_data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('time_zone', timezone_field.fields.TimeZoneField(default=b'UTC')),
                ('last_occurrence', models.DateTimeField(default=None, null=True)),
                ('next_occurrence', models.DateTimeField(default=None, null=True)),
                ('occurrence_handler_path', models.CharField(max_length=500)),
            ],
        ),
    ]
