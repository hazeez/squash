from django.db import models

# Create your models here.

class ProjectType(models.Model):
    type_name = models.CharField(max_length=3, primary_key=True)
    type_alias= models.CharField(max_length=3, blank=False)

    def __unicode__(self):
        return self.type_name

class RegionLeads(models.Model):
    regionlead_name = models.CharField(max_length=30, primary_key=True, blank=False)
    regionlead_alias = models.CharField(max_length=30, blank=False)

    def __unicode__(self):
        return self.regionlead_name

class SQAContactDatabase(models.Model):
    sqa_user_name = models.CharField(max_length=30, primary_key=True, blank=False)
    sqa_alias_name = models.CharField(max_length=30, blank=False)
    sqa_manager_name = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.sqa_user_name

class RegionDatabase(models.Model):
    region_code = models.CharField(max_length=4, blank=False, primary_key=True)
    region_alias = models.CharField(max_length=15, blank=False)

    def __unicode__(self):
        return self.region_code


class SubRegionDatabase(models.Model):

    REGIONS =  list((x.region_code, x.region_alias)for x in RegionDatabase.objects.all())
    REGIONLEADS =  list((x.regionlead_name, x.regionlead_alias)for x in RegionLeads.objects.all())

    sub_region_code = models.CharField(max_length=4, primary_key=True)
    sub_region_alias = models.CharField(max_length=15, blank=False)
    region = models.CharField(max_length=4, choices=REGIONS, default="EMEA")
    region_lead = models.CharField(max_length=30, blank=False, default='suniel.prabu', choices=REGIONLEADS)

    def __unicode__(self):
        return self.sub_region_alias

class ProjectStatus(models.Model):
    project_status_code = models.CharField(max_length=3, blank=False, primary_key=True)
    project_status_alias = models.CharField(max_length=15, blank=False)

    def __unicode__(self):
        return self.project_status_alias

class ReleaseStatus(models.Model):
    release_status_code = models.CharField(max_length=10, blank=False, primary_key=True)
    release_status_alias = models.CharField(max_length=20, blank=False)

    def __unicode__(self):
        return self.release_status_alias

class ProductDatabase(models.Model):
    product_code = models.CharField(max_length=15, blank=False, primary_key=True)
    product_alias = models.CharField(max_length=15, blank=False)

    def __unicode__(self):
        return self.product_code

class OptionChoice(models.Model):
    choice_code = models.CharField(max_length=3, primary_key=True)
    choice_alias = models.CharField(max_length=6, blank=False)

    def __unicode__(self):
        return self.choice_code

class ProjectDatabase(models.Model):
    PROJECT_TYPES =  list((x.type_name, x.type_alias)for x in ProjectType.objects.all())
    PROJECT_STATUSES = list((x.project_status_code, x.project_status_alias)for x in ProjectStatus.objects.all())
    RELEASE_STATUSES = list((x.release_status_code, x.release_status_alias)for x in ReleaseStatus.objects.all())
    REGIONS =  list((x.region_code, x.region_alias)for x in RegionDatabase.objects.all())
    SUBREGIONS = list((x.sub_region_code, x.sub_region_alias)for x in SubRegionDatabase.objects.all())
    SQANAMES = list((x.sqa_user_name, x.sqa_alias_name)for x in SQAContactDatabase.objects.all())
    PRODUCTS = list((x.product_code, x.product_alias)for x in ProductDatabase.objects.all())
    MANAGEDBY = (('SQA','SQA'),('PM','PM'))
    METHODS = (('PRLC','PRLC'),('OUM','OUM'),('APM','APM'))
    SCMTOOLS = (('SVN','SVN'),('VSS','VSS'))
    BUGTOOLS = (('JIRA','JIRA'),('BUGZ','BUGZ'),('CUST','CUST'))

    project_release_name = models.CharField(max_length=30, blank=False, primary_key=True)
    project_uid = models.CharField(max_length=15, blank=False, default="0")
    project_customer_name = models.CharField(max_length=40, blank=True, default="My Bank")
    project_class = models.CharField(max_length=3, blank=False, choices=PROJECT_TYPES, default="IUT")
    project_products = models.CharField(max_length=15, blank=False, choices=PRODUCTS, default="FCUBS")
    project_base_version = models.CharField(max_length=30, blank=False, default="No base")
    project_total_effort = models.IntegerField(default=0,blank=True)
    project_base_effort = models.IntegerField(default=0,blank=True)
    project_cut_effort = models.IntegerField(default=0,blank=True)
    project_testing_effort = models.IntegerField(default=0,blank=True)
    project_cob_effort = models.IntegerField(default=0,blank=True)
    project_status = models.CharField(max_length=9, blank=False, choices=PROJECT_STATUSES, default="ONG")
    project_manager = models.CharField(max_length=40, blank=True, default="PM Name")
    project_backup_manager = models.CharField(max_length=40, blank=True, default="No Manager")
    project_managed_by = models.CharField(max_length=3, default="SQA", choices = MANAGEDBY)
    project_primary_sqa = models.CharField(max_length=30, choices = SQANAMES, default="PM")
    project_secondary_sqa = models.CharField(max_length=30, blank=True, choices = SQANAMES, default="none")
    project_tertiary_sqa = models.CharField(max_length=30, blank=True, choices = SQANAMES, default="none")
    project_region_lead = models.CharField(max_length=30, blank=False, choices = SQANAMES, default="hafizul.azeez")
    project_region = models.CharField(max_length = 4, choices=REGIONS, blank = False, default="EMEA")
    project_subregion = models.CharField(max_length = 4, choices=SUBREGIONS, blank = False, default="AFRI")
    project_methodology = models.CharField(max_length=4, default="PRLC", choices = METHODS)
    project_created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    project_updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    project_start_date = models.DateField(blank=True,help_text="Please use the following format: <em>YYYY-MM-DD</em>.", default="1978-01-01")
    project_end_date = models.DateField(blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.", default="1978-01-01")
    project_duration = models.IntegerField(blank=True, default=0)
    project_description = models.TextField(max_length=1000, blank=True, default="None")
    project_scm_tool = models.CharField(max_length=3, default="SVN", choices=SCMTOOLS)
    project_scm_path = models.CharField(max_length=200, blank=True, default="path here")
    project_soft_path = models.CharField(max_length=200, blank=True, default="path here")
    project_bug_tool = models.CharField(max_length=4, default="JIRA", choices = BUGTOOLS)
    project_released_date = models.DateField(blank=True, null=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.",default="1978-01-01")
    project_release_status = models.CharField(max_length=10, blank=False, choices=RELEASE_STATUSES, default="PKOM")

    def __unicode__(self):
        return self.project_release_name + " >> " +self.project_uid

    class Meta:
        ordering = ('project_status',)

class ProjectReviewDetails(models.Model):
    CHOICES = list((x.choice_code, x.choice_alias)for x in OptionChoice.objects.all())

    release = models.ForeignKey(ProjectDatabase)

    # PKOM Details
    pkom_applicable = models.CharField(max_length=3, default="No", choices=CHOICES)
    order_shared = models.BooleanField(default=False)
    bpw_shared = models.BooleanField(default=False)
    pkom_checklist_shared = models.BooleanField(default=False)
    pkom_completed = models.BooleanField(default=False)

    #milestones
    plans_date = models.DateField(blank=True, default="1978-01-01")
    fs_date = models.DateField(blank=True, default="1978-01-01")
    ds_date = models.DateField(blank=True, default="1978-01-01")
    cut_start_date = models.DateField(blank=True, default="1978-01-01")
    cut_end_date = models.DateField(blank=True, default="1978-01-01")
    iut_start_date = models.DateField(blank=True, default="1978-01-01")
    iut_end_date = models.DateField(blank=True, default="1978-01-01")
    itr1_start_date = models.DateField(blank=True, default="1978-01-01")
    itr1_end_date = models.DateField(blank=True, default="1978-01-01")
    itr2_start_date = models.DateField(blank=True, default="1978-01-01")
    itr2_end_date = models.DateField(blank=True, default="1978-01-01")
    release_start_date = models.DateField(blank=True, default="1978-01-01")
    release_end_date = models.DateField(blank=True, default="1978-01-01")

    # Project Planning
    project_plans_applicable = models.CharField(max_length=3, default="No", choices=CHOICES)
    oum_estimator_baselined = models.BooleanField(default = False)
    oum_estimator_questionnaire_baselined = models.BooleanField(default = False)
    pmp_peer_reviewed = models.BooleanField(default=False)
    pmp_sme_reviewed = models.BooleanField(default=False)
    pmp_qmg_reviewed = models.BooleanField(default=False)
    pmp_baselined = models.BooleanField(default=False)
    mpp_peer_reviewed = models.BooleanField(default=False)
    mpp_qmg_reviewed = models.BooleanField(default=False)
    mpp_baselined = models.BooleanField(default=False)


    # RS related details
    rs_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    no_of_requirements = models.IntegerField(blank=True, default=0)


    # FS related details
    fs_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    fs_panel_review_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    fs_panel_review_mom_shared = models.BooleanField(default=False)
    applicable_fs_documents = models.IntegerField(blank=True, default=0)
    fs_signedoff = models.BooleanField(default=False)
    fs_peer_reviewed = models.BooleanField(default=False)
    fs_qmg_reviewed = models.BooleanField(default=False)
    fs_baselined = models.BooleanField(default=False)
    fs_documents_baselined = models.IntegerField(blank=True, default=0)

    # DS related details
    ds_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    applicable_ds_documents = models.IntegerField(default=0)
    ds_peer_reviewed = models.BooleanField(default=False)
    ds_qmg_reviewed = models.BooleanField(default=False)
    ds_baselined = models.BooleanField(default=False)
    ds_documents_baselined = models.IntegerField(blank=True, default=0)

    # PS related details
    ps_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    applicable_ps_documents = models.IntegerField(default=0)
    ps_peer_reviewed = models.BooleanField(default=False)
    ps_qmg_reviewed = models.BooleanField(default=False)
    ps_baselined = models.BooleanField(default=False)
    ps_documents_baselined = models.IntegerField(default=0)

    # UTP related details
    utp_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    utp_done_by_testing_team = models.BooleanField(default=False)
    utp_rounds = models.IntegerField(default=0)
    applicable_utp_documents = models.IntegerField(blank=True, default=0)
    utp_peer_reviewed = models.BooleanField(default=False)
    utp_qmg_reviewed = models.BooleanField(default=False)
    utp_baselined = models.BooleanField(default=False)
    utp_documents_baselined = models.IntegerField(blank=True, default=0)

    # code review related details
    code_applicable = models.CharField(choices=CHOICES, max_length=3, default="No",)
    code_peer_reviewed = models.BooleanField(default=False)
    code_qmg_reviewed = models.BooleanField(default=False)
    code_checkedin = models.BooleanField(default=False)
    total_units = models.IntegerField(blank=True, default=0)
    new_units = models.IntegerField(blank=True, default=0)

    #IUT bug reports
    iut_bug_report_obtained = models.BooleanField(default=False)
    iut_bug_report_baselined = models.BooleanField(default=False)
    iut_total_bugs = models.IntegerField(blank=True, default=0)
    iut_atype_bugs = models.IntegerField(blank=True, default=0)
    iut_btype_bugs = models.IntegerField(blank=True, default=0)
    iut_ctype_bugs = models.IntegerField(blank=True, default=0)
    iut_dtype_bugs = models.IntegerField(blank=True, default=0)
    iut_bugs_closed = models.BooleanField(default=False)
    iut_open_bug_details = models.TextField(max_length=200, blank=True)
    iut_rca_done = models.BooleanField(default=False)


    # Sampling related details
    sampling_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    sampling_completed = models.BooleanField(default=False)
    sampling_total_findings = models.IntegerField(default=0, blank=True)
    sampling_A_findings = models.IntegerField(default=0, blank=True)
    sampling_B_findings = models.IntegerField(default=0, blank=True)
    sampling_C_findings = models.IntegerField(default=0, blank=True)
    sampling_D_findings = models.IntegerField(default=0, blank=True)
    sampling_findings_closed = models.BooleanField(default=False)
    sampling_open_findings = models.TextField(max_length=200, blank=True)

    # CUT Audit
    cut_audit_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    cut_audit_completed = models.BooleanField(default=False)
    total_nc = models.IntegerField(blank=True, default=0)
    nc_major = models.IntegerField(blank=True, default=0)
    nc_minor = models.IntegerField(blank=True, default=0)
    nc_open = models.IntegerField(blank=True, default=0)
    nc_closed = models.IntegerField(blank=True, default=0)
    nc_details = models.TextField(max_length=1000, blank=True)

    #ITP
    it_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    no_of_itp = models.IntegerField(blank=True, default=0)
    no_of_itp_baselined = models.IntegerField(blank=True, default=0)
    itp_peer_review_done = models.BooleanField(default=False)
    itp_dev_review_done = models.BooleanField(default=False)
    itp_qmg_review_done = models.BooleanField(default = False)
    itp_review_comments_closed = models.BooleanField(default=False)

    # STP
    stp_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    stp_peer_reviewed = models.BooleanField(default=False)
    stp_dev_reviewed = models.BooleanField(default=False)
    stp_qmg_reviewed = models.BooleanField(default=False)
    stp_baselined = models.BooleanField(default=False)

    #ITR1 start
    itr1start_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    itr1_schema_details_obtained = models.BooleanField(default=False)
    itr1_code_checkedin = models.BooleanField(default=False)
    itr1_tps_checks_done = models.BooleanField(default=False)
    itr1_fortify_checks_done = models.BooleanField(default=False)
    itr1_start_email_sent = models.BooleanField(default=False)
    itr1start_tagging_done = models.BooleanField(default=False)

    #ITR1 Bugs
    itr1_bug_report_obtained = models.BooleanField(default=False)
    itr1_bug_report_baselined = models.BooleanField(default=False)
    itr1_total_bugs = models.IntegerField(blank=True, default=0)
    itr1_atype_bugs = models.IntegerField(blank=True, default=0)
    itr1_btype_bugs = models.IntegerField(blank=True, default=0)
    itr1_ctype_bugs = models.IntegerField(blank=True, default=0)
    itr1_dtype_bugs = models.IntegerField(blank=True, default=0)
    itr1_bugs_closed = models.BooleanField(default=False)
    itr1_open_bug_details = models.TextField(max_length=200, blank=True)
    itr1_rca_done = models.BooleanField(default=False)
    itr1_exit_criteria_baselined = models.BooleanField(default=False)

    #ITR1 Audits
    itr1_audit_completed = models.BooleanField(default=False)
    itr1_audit_total_issues = models.IntegerField(default=0)
    itr1_audit_open_issues = models.IntegerField(default=0)
    itr1_audit_closed_issues = models.IntegerField(default=0)
    itr1_audit_major_issues = models.IntegerField(default=0)
    itr1_audit_minor_issues = models.IntegerField(default=0)
    itr1_audit_details = models.TextField(max_length=200, blank=True)

    # Documentation
    user_manuals_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    help_files_applicable = models.BooleanField(default=False)
    um_peer_reviewed = models.BooleanField(default=False)
    um_testteam_reviewed = models.BooleanField(default=False)
    um_devteam_reviewed = models.BooleanField(default=False)
    um_qmg_reviewed = models.BooleanField(default=False)
    um_baselined = models.BooleanField(default=False)
    help_files_baselined = models.BooleanField(default=False)
    no_of_user_manuals = models.IntegerField(default = 0)

    #ITR2 start
    itr2start_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    itr2_code_checkedin = models.BooleanField(default=False)
    itr2_schema_details_obtained = models.BooleanField(default=False)
    itr2start_tagging_done = models.BooleanField(default=False)
    itr2_start_email_sent = models.BooleanField(default=False)

    #ITR2 Bugs
    itr2_bug_report_obtained = models.BooleanField(default=False)
    itr2_bug_report_baselined = models.BooleanField(default=False)
    itr2_total_bugs = models.IntegerField(blank=True, default=0)
    itr2_atype_bugs = models.IntegerField(blank=True, default=0)
    itr2_btype_bugs = models.IntegerField(blank=True, default=0)
    itr2_ctype_bugs = models.IntegerField(blank=True, default=0)
    itr2_dtype_bugs = models.IntegerField(blank=True, default=0)
    itr2_bugs_closed = models.BooleanField(default=False)
    itr2_open_bug_details = models.TextField(max_length=200, blank=True)
    itr2_rca_done = models.BooleanField(default=False)

    # Release
    itr2_tps_checks_done = models.BooleanField(default=False)
    itr2_fortify_checks_done = models.BooleanField(default=False)
    release_note_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    release_note_peer_reviewed = models.BooleanField(default=False)
    release_note_qmg_reviewed = models.BooleanField(default=False)
    release_note_baselined = models.BooleanField(default=False)
    dba_report_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    dba_report_peer_reviewed = models.BooleanField(default=False)
    dba_report_qmg_reviewed = models.BooleanField(default=False)
    dba_report_baselined = models.BooleanField(default=False)
    diff_report_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    diff_report_dev_reviewed = models.BooleanField(default=False)
    scm_report_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    scm_report_dev_reviewed =  models.BooleanField(default=False)
    scm_report_qmg_reviewed = models.BooleanField(default=False)
    itr2end_tagging_done = models.BooleanField(default=False)

    # Executables
    executables_applicable = models.CharField(choices=CHOICES, max_length=3, default="No")
    exec_dev_reviewed = models.BooleanField(default=False)
    exec_qmg_reviewed = models.BooleanField(default=False)
    exec_baselined = models.BooleanField(default=False)
    no_of_exec_baselined = models.IntegerField(default=0)
    draftrc_dev_reviewed = models.BooleanField(default=False)
    finalrc_sent = models.BooleanField(default=False)
    rc_baselined = models.BooleanField(default=False)

    def __unicode__(self):
        return self.release.project_release_name
