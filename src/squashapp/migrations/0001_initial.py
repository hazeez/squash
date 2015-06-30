# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDatabase',
            fields=[
                ('project_release_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('project_uid', models.CharField(max_length=12)),
                ('project_class', models.CharField(max_length=3, choices=[(b'IT', b'IT Release'), (b'IUT', b'IUT Release'), (b'CCB', b'Change Release')])),
                ('project_status', models.CharField(max_length=9, choices=[(b'ONG', b'Ongoing'), (b'ONH', b'On Hold'), (b'COM', b'Completed')])),
                ('project_primary_sqa', models.CharField(max_length=30)),
                ('project_region', models.CharField(max_length=10, choices=[(b'AM', b'Americas'), (b'JA', b'JAPAC'), (b'EU', b'Europe')])),
                ('project_created_date', models.DateTimeField(auto_now_add=True)),
                ('project_updated_date', models.DateTimeField(auto_now=True)),
                ('project_start_date', models.DateField(blank=True)),
                ('project_end_date', models.DateField(blank=True)),
                ('project_duration', models.DurationField(blank=True)),
            ],
        ),
    ]
