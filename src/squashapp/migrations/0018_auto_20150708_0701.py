# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0017_projectdatabase'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectReviewDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_of_requirements', models.IntegerField(max_length=3, blank=True)),
                ('applicable_fs_documents', models.IntegerField(max_length=3, blank=True)),
                ('fs_signedoff', models.BooleanField(default=False)),
                ('fs_peer_reviewed', models.BooleanField(default=False)),
                ('fs_qmg_reviewed', models.BooleanField(default=False)),
                ('fs_baselined', models.BooleanField(default=False)),
                ('fs_documents_baselined', models.IntegerField(max_length=3, blank=True)),
                ('applicable_ds_documents', models.IntegerField(max_length=3)),
                ('ds_peer_reviewed', models.BooleanField(default=False)),
                ('ds_qmg_reviewed', models.BooleanField(default=False)),
                ('ds_baselined', models.BooleanField(default=False)),
                ('ds_documents_baselined', models.IntegerField(max_length=3, blank=True)),
                ('ps_applicable', models.BooleanField(default=False)),
                ('applicable_ps_documents', models.IntegerField(default=0, max_length=3)),
                ('ps_peer_reviewed', models.BooleanField(default=False)),
                ('ps_qmg_reviewed', models.BooleanField(default=False)),
                ('ps_baselined', models.BooleanField(default=False)),
                ('ps_documents_baselined', models.IntegerField(default=0, max_length=3)),
                ('utp_done_by_testing_team', models.BooleanField(default=False)),
                ('utp_rounds', models.IntegerField(default=1, max_length=1)),
                ('applicable_utp_documents', models.IntegerField(max_length=3, blank=True)),
                ('utp_peer_reviewed', models.BooleanField(default=False)),
                ('utp_qmg_reviewed', models.BooleanField(default=False)),
                ('utp_baselined', models.BooleanField(default=False)),
                ('utp_documents_baselined', models.IntegerField(max_length=3, blank=True)),
                ('code_peer_reviewed', models.BooleanField(default=False)),
                ('code_qmg_reviewed', models.BooleanField(default=False)),
                ('code_checkedin', models.BooleanField(default=False)),
                ('code_units', models.IntegerField(max_length=3, blank=True)),
                ('sampling_completed', models.BooleanField(default=False)),
                ('sampling_total_findings', models.IntegerField(default=0, max_length=3, blank=True)),
                ('sampling_A_findings', models.IntegerField(default=0, max_length=2, blank=True)),
                ('sampling_B_findings', models.IntegerField(default=0, max_length=2, blank=True)),
                ('sampling_C_findings', models.IntegerField(default=0, max_length=2, blank=True)),
                ('sampling_D_findings', models.IntegerField(default=0, max_length=2, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_manager',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_released_date',
            field=models.DateField(help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_soft_path',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='projectdatabase',
            name='project_svn_path',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_description',
            field=models.TextField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_end_date',
            field=models.DateField(help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.', blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_region',
            field=models.CharField(max_length=4, choices=[('EMEA', 'EMEA'), ('AMER', 'Americas'), ('JAPC', 'Japan Asia Pac'), ('ALRE', 'All Regions')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_start_date',
            field=models.DateField(help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.', blank=True),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_subregion',
            field=models.CharField(max_length=4, choices=[('LATM', 'LATAM'), ('AMER', 'Americas'), ('MIEA', 'Middle East'), ('AFRI', 'Africa'), ('WEEU', 'Western Europe'), ('EAEU', 'Eastern Europe'), ('INDI', 'India'), ('SOEA', 'SouthEast Asia'), ('CITI', 'Citi'), ('BARC', 'Barclays'), ('ROJA', 'Rest of JAPAC')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='release_name',
            field=models.ForeignKey(to='squashapp.ProjectDatabase'),
        ),
    ]
