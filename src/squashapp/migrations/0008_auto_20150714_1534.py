# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0007_auto_20150714_1308'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectreviewdetails',
            old_name='ds_date',
            new_name='itr3_end_date',
        ),
        migrations.RenameField(
            model_name='projectreviewdetails',
            old_name='fs_date',
            new_name='itr3_start_date',
        ),
        migrations.RemoveField(
            model_name='projectreviewdetails',
            name='plans_date',
        ),
    ]
