# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0003_auto_20150713_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_end_date',
            field=models.DateField(default=b'1978-01-01', help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.', blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_start_date',
            field=models.DateField(default=b'1978-01-01', help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.', blank=True),
        ),
    ]
