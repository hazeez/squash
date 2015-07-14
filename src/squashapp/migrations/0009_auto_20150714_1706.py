# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0008_auto_20150714_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_release_name',
            field=models.CharField(max_length=40, serialize=False, primary_key=True),
        ),
    ]
