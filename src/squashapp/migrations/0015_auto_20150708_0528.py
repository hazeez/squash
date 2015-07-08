# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0014_auto_20150708_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubRegionDatabase',
            fields=[
                ('sub_region_code', models.CharField(max_length=4, serialize=False, primary_key=True)),
                ('sub_region_alias', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectDatabase',
        ),
        migrations.RemoveField(
            model_name='regiondatabase',
            name='sub_region_alias',
        ),
        migrations.RemoveField(
            model_name='regiondatabase',
            name='sub_region_code',
        ),
        migrations.AlterField(
            model_name='regiondatabase',
            name='region_code',
            field=models.CharField(max_length=4, serialize=False, primary_key=True),
        ),
    ]
