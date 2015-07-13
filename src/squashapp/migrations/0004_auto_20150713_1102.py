# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0003_auto_20150709_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectdatabase',
            old_name='project_svn_path',
            new_name='project_scm_path',
        ),
        migrations.RemoveField(
            model_name='projectdatabase',
            name='project_is_pm_managed',
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_backup_manager',
            field=models.CharField(default=b'No Manager', max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_base_version',
            field=models.CharField(default=b'No base', max_length=30),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_bug_tool',
            field=models.CharField(default=b'JIRA', max_length=4, choices=[(b'JIRA', b'JIRA'), (b'BUGZ', b'BUGZ'), (b'CUST', b'CUST')]),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_cob_effort',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_customer_name',
            field=models.CharField(default=b'My Bank', max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_cut_effort',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_managed_by',
            field=models.CharField(default=b'SQA', max_length=3, choices=[(b'SQA', b'SQA'), (b'PM', b'PM')]),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_methodology',
            field=models.CharField(default=b'PRLC', max_length=4, choices=[(b'PRLC', b'PRLC'), (b'OUM', b'OUM'), (b'APM', b'APM')]),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_scm_tool',
            field=models.CharField(default=b'SVN', max_length=3, choices=[(b'SVN', b'SVN'), (b'VSS', b'VSS')]),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_testing_effort',
            field=models.IntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_total_effort',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
