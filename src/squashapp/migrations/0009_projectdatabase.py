# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0008_auto_20150707_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDatabase',
            fields=[
                ('project_release_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('project_uid', models.CharField(max_length=15)),
                ('project_class', models.CharField(max_length=3, choices=[('IT', 'IT'), ('IUT', 'IUT'), ('CCB', 'CCB')])),
                ('project_primary_sqa', models.CharField(max_length=30)),
                ('project_secondary_sqa', models.CharField(max_length=30, blank=True)),
                ('project_tertiary_sqa', models.CharField(max_length=30, blank=True)),
                ('project_region_lead', models.CharField(max_length=30)),
                ('project_created_date', models.DateTimeField(auto_now_add=True)),
                ('project_updated_date', models.DateTimeField(auto_now=True)),
                ('project_start_date', models.DateField(blank=True)),
                ('project_end_date', models.DateField(blank=True)),
                ('project_duration', models.IntegerField(blank=True)),
            ],
        ),
    ]
