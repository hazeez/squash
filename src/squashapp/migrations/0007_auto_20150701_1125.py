# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0006_auto_20150701_1113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectdatabase',
            options={'ordering': ('project_updated_date',)},
        ),
    ]
