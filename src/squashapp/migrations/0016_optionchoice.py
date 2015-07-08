# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0015_auto_20150708_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionChoice',
            fields=[
                ('choice_code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('choice_alias', models.CharField(max_length=6)),
            ],
        ),
    ]
