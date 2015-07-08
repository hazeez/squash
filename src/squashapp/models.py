from django.db import models

# Create your models here.

class ProjectType(models.Model):
    type_name = models.CharField(max_length=3, primary_key=True)
    type_alias= models.CharField(max_length=3, blank=False)

    def __unicode__(self):
        return self.type_name

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
    sub_region_code = models.CharField(max_length=4, primary_key=True)
    sub_region_alias = models.CharField(max_length=15, blank=False)

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
    project_class = models.CharField(max_length=3, blank=False, choices=PROJECT_TYPES)
    project_products = models.CharField(max_length=15, blank=False, choices=PRODUCTS)
    project_status = models.CharField(max_length=9, blank=False, choices=PROJECT_STATUSES)
    project_manager = models.CharField(max_length=40, blank=True)
    project_primary_sqa = models.CharField(max_length=30, choices = SQANAMES)
    project_secondary_sqa = models.CharField(max_length=30, blank=True, choices = SQANAMES)
    project_tertiary_sqa = models.CharField(max_length=30, blank=True, choices = SQANAMES)
    project_region_lead = models.CharField(max_length=30, blank=False, choices = SQANAMES)
    project_region = models.CharField(max_length = 4, choices=REGIONS, blank = False)
    project_subregion = models.CharField(max_length = 4, choices=SUBREGIONS, blank = False)
    project_created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    project_updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    project_start_date = models.DateField(blank=True,help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    project_end_date = models.DateField(blank=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    project_release_status = models.CharField(max_length=10, blank=False, choices=RELEASE_STATUSES)
    project_duration = models.IntegerField(blank=True)
    project_is_pm_managed = models.BooleanField(default=False)
    project_description = models.TextField(max_length=1000, blank=True)
    project_svn_path = models.CharField(max_length=200, blank=True)
    project_soft_path = models.CharField(max_length=200, blank=True)
    project_released_date = models.DateField(blank=True, null=True, help_text="Please use the following format: <em>YYYY-MM-DD</em>.")

    def __unicode__(self):
        return self.project_uid

    class Meta:
        ordering = ('project_status',)

class ProjectReviewDetails(models.Model):
    release_name = models.ForeignKey(ProjectDatabase)
    # RS related details
    no_of_requirements = models.IntegerField(blank=True)

    # FS related details
    applicable_fs_documents = models.IntegerField(blank=True)
    fs_signedoff = models.BooleanField(default=False)
    fs_peer_reviewed = models.BooleanField(default=False)
    fs_qmg_reviewed = models.BooleanField(default=False)
    fs_baselined = models.BooleanField(default=False)
    fs_documents_baselined = models.IntegerField(blank=True)

    # DS related details
    applicable_ds_documents = models.IntegerField()
    ds_peer_reviewed = models.BooleanField(default=False)
    ds_qmg_reviewed = models.BooleanField(default=False)
    ds_baselined = models.BooleanField(default=False)
    ds_documents_baselined = models.IntegerField(blank=True)

    # PS related details
    ps_applicable = models.BooleanField(default=False)
    applicable_ps_documents = models.IntegerField(default=0)
    ps_peer_reviewed = models.BooleanField(default=False)
    ps_qmg_reviewed = models.BooleanField(default=False)
    ps_baselined = models.BooleanField(default=False)
    ps_documents_baselined = models.IntegerField(default=0)

    # UTP related details
    utp_done_by_testing_team = models.BooleanField(default=False)
    utp_rounds = models.IntegerField(default=1)
    applicable_utp_documents = models.IntegerField(blank=True)
    utp_peer_reviewed = models.BooleanField(default=False)
    utp_qmg_reviewed = models.BooleanField(default=False)
    utp_baselined = models.BooleanField(default=False)
    utp_documents_baselined = models.IntegerField(blank=True)

    # code review related details
    code_peer_reviewed = models.BooleanField(default=False)
    code_qmg_reviewed = models.BooleanField(default=False)
    code_checkedin = models.BooleanField(default=False)
    code_units = models.IntegerField(blank=True)

    # CUT Audit and Sampling related details
    sampling_completed = models.BooleanField(default=False)
    sampling_total_findings = models.IntegerField(default=0, blank=True)
    sampling_A_findings = models.IntegerField(default=0, blank=True)
    sampling_B_findings = models.IntegerField(default=0, blank=True)
    sampling_C_findings = models.IntegerField(default=0, blank=True)
    sampling_D_findings = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.release_name
