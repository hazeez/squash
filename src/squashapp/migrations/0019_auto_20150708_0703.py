# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0018_auto_20150708_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='applicable_ds_documents',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='applicable_fs_documents',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='applicable_ps_documents',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='applicable_utp_documents',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='code_units',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='ds_documents_baselined',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='fs_documents_baselined',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='no_of_requirements',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='sampling_total_findings',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='utp_documents_baselined',
            field=models.IntegerField(blank=True),
        ),
    ]
