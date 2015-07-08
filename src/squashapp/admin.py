from django.contrib import admin
from .models import ProjectType, SQAContactDatabase, RegionDatabase, SubRegionDatabase, ProjectStatus, ReleaseStatus, ProductDatabase, OptionChoice, ProjectDatabase, ProjectReviewDetails

# Register your models here.
admin.site.register(ProjectDatabase)
admin.site.register(ProjectReviewDetails)
admin.site.register(ProjectType)
admin.site.register(SQAContactDatabase)
admin.site.register(RegionDatabase)
admin.site.register(SubRegionDatabase)
admin.site.register(ProjectStatus)
admin.site.register(ReleaseStatus)
admin.site.register(ProductDatabase)
admin.site.register(OptionChoice)
