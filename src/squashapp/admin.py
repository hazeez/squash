from django.contrib import admin
from .models import ProjectType, SQAContactDatabase, RegionDatabase, SubRegionDatabase, ProjectStatus, ReleaseStatus, ProductDatabase, OptionChoice, ProjectDatabase, ProjectReviewDetails, RegionLeads

# Register your models here.
admin.site.register(ProjectDatabase)
admin.site.register(ProjectReviewDetails)
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

admin.site.register(SubRegionDatabase, SubRegionDatabaseAdmin )
admin.site.register(SQAContactDatabase, SQAContactDatabaseAdmin)
