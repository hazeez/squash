# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0019_auto_20150708_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='sampling_A_findings',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='sampling_B_findings',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='sampling_C_findings',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='sampling_D_findings',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
