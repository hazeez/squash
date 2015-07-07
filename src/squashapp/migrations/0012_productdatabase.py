# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0011_auto_20150707_1559'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDatabase',
            fields=[
                ('product_code', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('product_alias', models.CharField(max_length=15)),
            ],
        ),
    ]
