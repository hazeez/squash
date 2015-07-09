# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectreviewdetails',
            old_name='audit_report_sent',
            new_name='itr1_audit_completed',
        ),
        migrations.RenameField(
            model_name='projectreviewdetails',
            old_name='itr2_qmg_email_sent',
            new_name='itr2_start_email_sent',
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_audit_closed_issues',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_audit_details',
            field=models.TextField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_audit_major_issues',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_audit_minor_issues',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_audit_open_issues',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_audit_total_issues',
            field=models.IntegerField(default=0),
        ),
    ]
