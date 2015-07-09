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

    project_release_name = models.CharField(max_length=30, blank=False, primary_key=True)
    project_uid = models.CharField(max_length=15, blank=False)
    project_class = models.CharField(max_length=3, blank=False, choices=PROJECT_TYPES, default="IUT")
    project_products = models.CharField(max_length=15, blank=False, choices=PRODUCTS, default="FCUBS")
    project_status = models.CharField(max_length=9, blank=False, choices=PROJECT_STATUSES, default="ONG")
    project_manager = models.CharField(max_length=40, blank=True)
    project_primary_sqa = models.CharField(max_length=30, choices = SQANAMES, default="hafizul.azeez")
    project_secondary_sqa = models.CharField(max_length=30, blank=True, choices = SQANAMES, default="hafizul.azeez")
    project_tertiary_sqa = models.CharField(max_length=30, blank=True, choices = SQANAMES, default="hafizul.azeez")
    project_region_lead = models.CharField(max_length=30, blank=False, choices = SQANAMES, default="hafizul.azeez")
    project_region = models.CharField(max_length = 4, choices=REGIONS, blank = False, default="EMEA")
    project_subregion = models.CharField(max_length = 4, choices=SUBREGIONS, blank = False, default="AFRI")
    project_created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    project_updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    project_start_date = models.DateField(blank=True,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    project_end_date = models.DateField(blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    project_release_status = models.CharField(max_length=10, blank=False, choices=RELEASE_STATUSES, default="PKOM")
    project_duration = models.IntegerField(blank=True)
    project_is_pm_managed = models.BooleanField(default=False)
    project_description = models.TextField(max_length=1000, blank=True)
    project_svn_path = models.CharField(max_length=200, blank=True)
    project_soft_path = models.CharField(max_length=200, blank=True)
    project_released_date = models.DateField(blank=True, null=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    def __unicode__(self):
        return self.project_release_name , self.project_uid

    class Meta:
        ordering = ('project_status',)

class ProjectReviewDetails(models.Model):
    CHOICES = list((x.choice_code, x.choice_alias)for x in OptionChoice.objects.all())

    release_name = models.ForeignKey(ProjectDatabase)
    # RS related details
    rs_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    no_of_requirements = models.IntegerField(blank=True)


    # FS related details
    fs_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    applicable_fs_documents = models.IntegerField(blank=True)
    fs_signedoff = models.BooleanField(default=False)
    fs_peer_reviewed = models.BooleanField(default=False)
    fs_qmg_reviewed = models.BooleanField(default=False)
    fs_baselined = models.BooleanField(default=False)
    fs_documents_baselined = models.IntegerField(blank=True)

    # DS related details
    ds_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    applicable_ds_documents = models.IntegerField()
    ds_peer_reviewed = models.BooleanField(default=False)
    ds_qmg_reviewed = models.BooleanField(default=False)
    ds_baselined = models.BooleanField(default=False)
    ds_documents_baselined = models.IntegerField(blank=True)

    # PS related details
    ps_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    applicable_ps_documents = models.IntegerField(default=0)
    ps_peer_reviewed = models.BooleanField(default=False)
    ps_qmg_reviewed = models.BooleanField(default=False)
    ps_baselined = models.BooleanField(default=False)
    ps_documents_baselined = models.IntegerField(default=0)

    # UTP related details
    utp_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    utp_done_by_testing_team = models.BooleanField(default=False)
    utp_rounds = models.IntegerField(default=1)
    applicable_utp_documents = models.IntegerField(blank=True)
    utp_peer_reviewed = models.BooleanField(default=False)
    utp_qmg_reviewed = models.BooleanField(default=False)
    utp_baselined = models.BooleanField(default=False)
    utp_documents_baselined = models.IntegerField(blank=True)

    # code review related details
    code_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes",)
    code_peer_reviewed = models.BooleanField(default=False)
    code_qmg_reviewed = models.BooleanField(default=False)
    code_checkedin = models.BooleanField(default=False)
    total_units = models.IntegerField(blank=True)
    new_units = models.IntegerField(blank=True)

    #IUT bug reports
    iut_bug_report_obtained = models.BooleanField(default=False)
    iut_bug_report_baselined = models.BooleanField(default=False)
    iut_total_bugs = models.IntegerField(blank=True)
    iut_atype_bugs = models.IntegerField(blank=True)
    iut_btype_bugs = models.IntegerField(blank=True)
    iut_ctype_bugs = models.IntegerField(blank=True)
    iut_dtype_bugs = models.IntegerField(blank=True)
    iut_bugs_closed = models.BooleanField(default=False)
    iut_open_bug_details = models.TextField(max_length=200, blank=True)
    iut_rca_done = models.BooleanField(default=False)


    # Sampling related details
    sampling_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    sampling_completed = models.BooleanField(default=False)
    sampling_total_findings = models.IntegerField(default=0, blank=True)
    sampling_A_findings = models.IntegerField(default=0, blank=True)
    sampling_B_findings = models.IntegerField(default=0, blank=True)
    sampling_C_findings = models.IntegerField(default=0, blank=True)
    sampling_D_findings = models.IntegerField(default=0, blank=True)
    sampling_findings_closed = models.BooleanField(default=False)
    sampling_open_findings = models.TextField(max_length=200, blank=True)

    # CUT Audit
    cut_audit_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    cut_audit_completed = models.BooleanField(default=False)
    total_nc = models.IntegerField(blank=True)
    nc_major = models.IntegerField(blank=True)
    nc_minor = models.IntegerField(blank=True)
    nc_open = models.IntegerField(blank=True)
    nc_closed = models.IntegerField(blank=True)
    nc_details = models.TextField(max_length=1000, blank=True)

    #ITP
    it_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    no_of_itp = models.IntegerField(blank=True)
    no_of_itp_baselined = models.IntegerField(blank=True)
    itp_peer_review_done = models.BooleanField(default=False)
    itp_dev_review_done = models.BooleanField(default=False)
    itp_qmg_review_done = models.BooleanField(default = False)
    itp_review_comments_closed = models.BooleanField(default=False)

    #ITR1 start
    itr1start_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    itr1_schema_details_obtained = models.BooleanField(default=False)
    itr1start_tagging_done = models.BooleanField(default=False)
    itr1_code_checkedin = models.BooleanField(default=False)
    itr1_tps_checks_done = models.BooleanField(default=False)
    itr1_fortify_checks_done = models.BooleanField(default=False)
    itr1_start_email_sent = models.BooleanField(default=False)

    #ITR1 Bugs
    itr1_bug_report_obtained = models.BooleanField(default=False)
    itr1_bug_report_baselined = models.BooleanField(default=False)
    itr1_total_bugs = models.IntegerField(blank=True)
    itr1_atype_bugs = models.IntegerField(blank=True)
    itr1_btype_bugs = models.IntegerField(blank=True)
    itr1_ctype_bugs = models.IntegerField(blank=True)
    itr1_dtype_bugs = models.IntegerField(blank=True)
    itr1_bugs_closed = models.BooleanField(default=False)
    itr1_open_bug_details = models.TextField(max_length=200, blank=True)
    itr1_rca_done = models.BooleanField(default=False)

    #ITR1 Audits
    itr1_audit_completed = models.BooleanField(default=False)
    itr1_audit_total_issues = models.IntegerField(default=0)
    itr1_audit_open_issues = models.IntegerField(default=0)
    itr1_audit_closed_issues = models.IntegerField(default=0)
    itr1_audit_major_issues = models.IntegerField(default=0)
    itr1_audit_minor_issues = models.IntegerField(default=0)
    itr1_audit_details = models.TextField(max_length=200, blank=True)

    #ITR2 start
    itr2start_applicable = models.CharField(choices=CHOICES, max_length=3, default="Yes")
    itr2_code_checkedin = models.BooleanField(default=False)
    itr2_schema_details_obtained = models.BooleanField(default=False)
    itr2start_tagging_done = models.BooleanField(default=False)
    itr2_tps_checks_done = models.BooleanField(default=False)
    itr2_fortify_checks_done = models.BooleanField(default=False)
    itr2_start_email_sent = models.BooleanField(default=False)

    #ITR2 Bugs
    itr2_bug_report_obtained = models.BooleanField(default=False)
    itr2_bug_report_baselined = models.BooleanField(default=False)
    itr2_total_bugs = models.IntegerField(blank=True)
    itr2_atype_bugs = models.IntegerField(blank=True)
    itr2_btype_bugs = models.IntegerField(blank=True)
    itr2_ctype_bugs = models.IntegerField(blank=True)
    itr2_dtype_bugs = models.IntegerField(blank=True)
    itr2_bugs_closed = models.BooleanField(default=False)
    itr2_open_bug_details = models.TextField(max_length=200, blank=True)
    itr2_rca_done = models.BooleanField(default=False)

    def __unicode__(self):
        return self.release_name
