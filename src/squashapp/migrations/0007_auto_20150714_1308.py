# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0006_auto_20150713_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='release',
            field=models.ForeignKey(related_name='project_details', to='squashapp.ProjectDatabase'),
        ),
    ]
