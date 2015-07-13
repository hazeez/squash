# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('squashapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectdatabase',
            old_name='project_svn_path',
            new_name='project_scm_path',
        ),
        migrations.RenameField(
            model_name='projectreviewdetails',
            old_name='audit_report_sent',
            new_name='bpw_shared',
        ),
        migrations.RenameField(
            model_name='projectreviewdetails',
            old_name='itr2_qmg_email_sent',
            new_name='dba_report_baselined',
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
        migrations.AddField(
            model_name='projectreviewdetails',
            name='cut_end_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='cut_start_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='dba_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='dba_report_peer_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='dba_report_qmg_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='diff_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='diff_report_dev_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='draftrc_dev_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='exec_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='exec_dev_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='exec_qmg_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='executables_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='finalrc_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='fs_panel_review_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='fs_panel_review_mom_shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='help_files_applicable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='help_files_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_audit_closed_issues',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_audit_completed',
            field=models.BooleanField(default=False),
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
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_end_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_exit_criteria_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr1_start_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr2_end_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr2_start_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr2_start_email_sent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='itr2end_tagging_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='iut_end_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='iut_start_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='mpp_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='mpp_peer_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='mpp_qmg_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='no_of_exec_baselined',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='no_of_user_manuals',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='order_shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='oum_estimator_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='oum_estimator_questionnaire_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='pkom_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='pkom_checklist_shared',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='pkom_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='pmp_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='pmp_peer_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='pmp_qmg_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='pmp_sme_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='project_plans_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='rc_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='release_end_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='release_note_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='release_note_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='release_note_peer_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='release_note_qmg_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='release_start_date',
            field=models.DateField(default=b'1978-01-01', blank=True),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='scm_report_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='scm_report_dev_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='scm_report_qmg_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='stp_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='stp_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='stp_dev_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='stp_peer_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='stp_qmg_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='um_baselined',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='um_devteam_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='um_peer_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='um_qmg_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='um_testteam_reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectreviewdetails',
            name='user_manuals_applicable',
            field=models.CharField(default=b'No', max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_class',
            field=models.CharField(default=b'IUT', max_length=3, choices=[('IT', 'IT'), ('IUT', 'IUT'), ('CCB', 'CCB'), ('TEM', 'TEM')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_primary_sqa',
            field=models.CharField(default=b'PM', max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_products',
            field=models.CharField(default=b'FCUBS', max_length=15, choices=[('FCUBS', 'FCUBS'), ('FCDB', 'FCDB'), ('FCIS', 'FCIS'), ('FCELCM', 'FCELCM'), ('FCPB', 'FCPB'), ('FCR', 'FCR'), ('FC@', 'FC@'), ('FCC', 'FCC')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_region',
            field=models.CharField(default=b'EMEA', max_length=4, choices=[('EMEA', 'EMEA'), ('AMER', 'Americas'), ('JAPC', 'Japan Asia Pac'), ('FCIS', 'FCIS'), ('FCPB', 'FCPB'), ('CITI', 'CITI'), ('BARC', 'Barclays')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_region_lead',
            field=models.CharField(default=b'hafizul.azeez', max_length=30, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_release_status',
            field=models.CharField(default=b'PKOM', max_length=10, choices=[('PKOM', 'PKOM'), ('CUTSTART', 'CUT START'), ('CUTEND', 'CUT END'), ('ITR1START', 'ITR1 START'), ('ITR2START', 'ITR2 START'), ('ITR2END', 'ITR2 END'), ('PREREL', 'Pre Release'), ('RELEASED', 'Released')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_secondary_sqa',
            field=models.CharField(default=b'none', max_length=30, blank=True, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_status',
            field=models.CharField(default=b'ONG', max_length=9, choices=[('ONG', 'Ongoing'), ('COM', 'Completed'), ('ONH', 'OnHold'), ('DRP', 'Dropped')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_subregion',
            field=models.CharField(default=b'AFRI', max_length=4, choices=[('LATM', 'LATAM'), ('AMER', 'Americas'), ('MIEA', 'Middle East'), ('AFRI', 'Africa'), ('WEEU', 'Western Europe'), ('EAEU', 'Eastern Europe'), ('INDI', 'India'), ('SOEA', 'SouthEast Asia'), ('CITI', 'Citi'), ('BARC', 'Barclays'), ('ROJA', 'Rest of JAPAC')]),
        ),
        migrations.AlterField(
            model_name='projectdatabase',
            name='project_tertiary_sqa',
            field=models.CharField(default=b'none', max_length=30, blank=True, choices=[('hafizul.azeez', 'hafizul.azeez'), ('pratik.ravani', 'pratik.ravani'), ('sharmila.subramani', 'sharmila.subramani'), ('chandrasekhar.paramanantham', 'chandrasekhar.paramanantham'), ('obi.ravi', 'obi.ravi'), ('kedar.chaudhari', 'kedar.chaudhari'), ('rahatul.huda', 'rahatul.huda'), ('nerissa.rodrigues', 'nerissa.rodrigues'), ('suniel.prabu', 'suniel.prabu'), ('amit.parte', 'amit.parte'), ('priyanka.pandey', 'priyanka.pandey'), ('sunanda.mishra', 'sunanda.mishra'), ('nayana.siddappa', 'nayana.siddappa'), ('tripti.prasad', 'tripti.prasad'), ('prasanna.jain', 'prasanna.jain')]),
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
            name='ps_applicable',
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
