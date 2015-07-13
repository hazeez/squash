# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0004_auto_20150713_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_description',
            field=models.TextField(default=b'None', max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_duration',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_manager',
            field=models.CharField(default=b'PM Name', max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_released_date',
            field=models.DateField(default=b'1978-01-01', help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_scm_path',
            field=models.CharField(default=b'path here', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_soft_path',
            field=models.CharField(default=b'path here', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_uid',
            field=models.CharField(default=b'0', max_length=15),
        ),
    ]
