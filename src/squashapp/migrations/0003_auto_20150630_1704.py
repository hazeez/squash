# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0002_auto_20150630_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_class',
            field=models.CharField(max_length=3, choices=[(b'IT', b'IT'), (b'IUT', b'IUT'), (b'CCB', b'CCB')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_duration',
            field=models.IntegerField(max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_uid',
            field=models.CharField(max_length=15),
        ),
    ]
