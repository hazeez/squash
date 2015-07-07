# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0007_auto_20150701_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('Type_Name', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('Type_Alias', models.CharField(max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectDatabase',
        ),
    ]
