# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0021_auto_20150708_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='ps_documents_baselined',
            field=models.IntegerField(default=0),
        ),
    ]
