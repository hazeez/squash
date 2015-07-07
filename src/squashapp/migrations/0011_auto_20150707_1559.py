# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0010_auto_20150707_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseStatus',
            fields=[
                ('release_status_code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('release_status_alias', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='projectstatus',
            old_name='status_alias',
            new_name='project_status_alias',
        ),
        migrations.RenameField(
            model_name='projectstatus',
            old_name='status_code',
            new_name='project_status_code',
        ),
    ]
