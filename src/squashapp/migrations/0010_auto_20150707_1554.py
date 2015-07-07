# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0009_projectdatabase'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('status_code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('status_alias', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RegionDatabase',
            fields=[
                ('sub_region_code', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('sub_region_alias', models.CharField(max_length=15)),
                ('region_code', models.CharField(max_length=4)),
                ('region_alias', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='SQAContactDatabase',
            fields=[
                ('sqa_user_name', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('sqa_alias_name', models.CharField(max_length=30)),
                ('sqa_manager_name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectDatabase',
        ),
        migrations.RenameField(
            model_name='projecttype',
            old_name='Type_Alias',
            new_name='type_alias',
        ),
        migrations.RenameField(
            model_name='projecttype',
            old_name='Type_Name',
            new_name='type_name',
        ),
    ]
