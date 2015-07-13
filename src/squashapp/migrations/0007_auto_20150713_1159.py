# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0006_auto_20150713_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectreviewdetails',
            name='no_of_exec_baselined',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='applicable_ds_documents',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='applicable_fs_documents',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='code_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='cut_audit_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='dba_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='diff_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='ds_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='ds_documents_baselined',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='executables_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='fs_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='fs_documents_baselined',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='it_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr1_atype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr1_btype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr1_ctype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr1_dtype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr1_total_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr1start_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='itr2start_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='iut_atype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='iut_btype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='iut_ctype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='iut_dtype_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='iut_total_bugs',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='nc_closed',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='nc_major',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='nc_minor',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='nc_open',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='new_units',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='no_of_itp',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='no_of_itp_baselined',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='no_of_requirements',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='pkom_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='project_plans_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='ps_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='release_note_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='rs_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='sampling_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='scm_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='stp_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='total_nc',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='total_units',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='user_manuals_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='utp_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='utp_documents_baselined',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AlterField(
            model_name='projectreviewdetails',
            name='utp_rounds',
            field=models.IntegerField(default=0),
        ),
    ]
