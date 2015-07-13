# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0002_auto_20150713_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdatabase',
            name='project_base_effort',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='ds_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='fs_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='plans_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='code_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='cut_audit_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='dba_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='diff_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='ds_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='executables_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='fs_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='fs_panel_review_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='it_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr1start_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr2start_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='pkom_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='project_plans_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='ps_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='release_note_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='rs_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='sampling_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='scm_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='stp_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='user_manuals_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='utp_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No'), ('NA', 'NA')]),
        ),
    ]
