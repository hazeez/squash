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
    sub_region_code = models.CharField(max_length=4, primary_key=True)
    sub_region_alias = models.CharField(max_length=15, blank=False)
    region_code = models.CharField(max_length=4, blank=False)
    region_alias = models.CharField(max_length=15, blank=False)

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

class ProjectDatabase(models.Model):
    PROJECT_TYPES =  list((x.type_name, x.type_alias)for x in ProjectType.objects.all())
    PROJECT_STATUSES = list((x.project_status_code, x.project_status_alias)for x in ProjectStatus.objects.all())
    RELEASE_STATUSES = list((x.release_status_code, x.release_status_alias)for x in ReleaseStatus.objects.all())
    REGIONS =  list((x.region_code, x.region_alias)for x in RegionDatabase.objects.all())
    SUBREGIONS = list((x.sub_region_code, x.sub_region_alias)for x in RegionDatabase.objects.all())
    SQANAMES = list((x.sqa_user_name, x.sqa_alias_name)for x in SQAContactDatabase.objects.all())
    PRODUCTS = list((x.product_code, x.product_alias)for x in ProductDatabase.objects.all())

    project_release_name = models.CharField(max_length=30, blank=False, primary_key=True)
    project_uid = models.CharField(max_length=15, blank=False)
    project_class = models.CharField(max_length=3, blank=False, choices=PROJECT_TYPES)
    project_products = models.CharField(max_length=15, blank=False, choices=PRODUCTS)
    project_status = models.CharField(max_length=9, blank=False, choices=PROJECT_STATUSES)
    project_primary_sqa = models.CharField(max_length=30, choices = SQANAMES)
    project_secondary_sqa = models.CharField(max_length=30, blank=True, choices = SQANAMES)
    project_tertiary_sqa = models.CharField(max_length=30, blank=True, choices = SQANAMES)
    project_region_lead = models.CharField(max_length=30, blank=False, choices = SQANAMES)
    project_region = models.CharField(max_length = 4, choices=REGIONS, blank = False)
    project_subregion = models.CharField(max_length = 4, choices=SUBREGIONS, blank = False)
    project_created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    project_updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    project_start_date = models.DateField(blank=True)
    project_end_date = models.DateField(blank=True)
    project_release_status = models.CharField(max_length=10, blank=False, choices=RELEASE_STATUSES)
    project_duration = models.IntegerField(blank=True)


    def __unicode__(self):
        return self.project_release_name

    class Meta:
        ordering = ('project_status',)

