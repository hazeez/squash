from django.db import models

# Create your models here.
class ProjectDatabase(models.Model):
    PROJECT_TYPES = (('IT','IT'),('IUT','IUT'),('CCB','CCB'),)
    PROJECT_STATUSES = (('ONG','Ongoing'), ('ONH','On Hold'),('COM','Completed'),)
    REGIONS = (('AME','Americas'), ('JAP','JAPAC'),('EUR','Europe'),)

    project_release_name = models.CharField(max_length=30, blank=False, primary_key=True)
    project_uid = models.CharField(max_length=15, blank=False)
    project_class = models.CharField(max_length=3, blank=False, choices=PROJECT_TYPES)
    project_status = models.CharField(max_length=9, blank=False, choices=PROJECT_STATUSES)
    project_primary_sqa = models.CharField(max_length=30)
    project_region = models.CharField(max_length = 3, choices=REGIONS, blank = False)
    project_created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    project_updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    project_start_date = models.DateField(blank=True)
    project_end_date = models.DateField(blank=True)
    project_duration = models.IntegerField(blank=True)


    def __unicode__(self):
        return self.project_release_name
