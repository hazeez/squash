# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0020_auto_20150708_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='utp_rounds',
            field=models.IntegerField(default=1),
        ),
    ]
