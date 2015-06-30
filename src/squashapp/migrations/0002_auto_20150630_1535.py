# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_region',
            field=models.CharField(max_length=3, choices=[(b'AME', b'Americas'), (b'JAP', b'JAPAC'), (b'EUR', b'Europe')]),
        ),
    ]
