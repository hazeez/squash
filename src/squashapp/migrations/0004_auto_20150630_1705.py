# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0003_auto_20150630_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_duration',
            field=models.IntegerField(blank=True),
        ),
    ]
