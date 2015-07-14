from django.contrib import admin
from .models import ProjectType, SQAContactDatabase, RegionDatabase, SubRegionDatabase, ProjectStatus, ReleaseStatus, ProductDatabase, OptionChoice, ProjectDatabase, ProjectReviewDetails, RegionLeads

# Register your models here.

admin.site.register(ProjectType)
admin.site.register(RegionLeads)
admin.site.register(RegionDatabase)

admin.site.register(ProjectStatus)
admin.site.register(ReleaseStatus)
admin.site.register(ProductDatabase)
admin.site.register(OptionChoice)


class SubRegionDatabaseAdmin(admin.ModelAdmin):
    list_display = ['sub_region_code','sub_region_alias','region','region_lead']


class SQAContactDatabaseAdmin(admin.ModelAdmin):
    list_display = ['sqa_user_name','sqa_manager_name']

class ProjectDatabaseAdmin(admin.ModelAdmin):
    list_display = ['project_release_name','project_uid','project_products','project_class','project_manager','project_managed_by','project_start_date','project_end_date',]

class ProjectReviewDetailsAdmin(admin.ModelAdmin):
    list_display = ['release','cut_start_date','cut_end_date','iut_start_date','iut_end_date',]

admin.site.register(SubRegionDatabase, SubRegionDatabaseAdmin )
admin.site.register(SQAContactDatabase, SQAContactDatabaseAdmin)
admin.site.register(ProjectDatabase, ProjectDatabaseAdmin)
admin.site.register(ProjectReviewDetails, ProjectReviewDetailsAdmin)
