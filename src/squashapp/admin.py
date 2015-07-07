from django.contrib import admin
from .models import ProjectType, SQAContactDatabase, RegionDatabase, ProjectStatus, ReleaseStatus, ProductDatabase, ProjectDatabase

# Register your models here.
admin.site.register(ProjectDatabase)
admin.site.register(ProjectType)
admin.site.register(SQAContactDatabase)
admin.site.register(RegionDatabase)
admin.site.register(ProjectStatus)
admin.site.register(ReleaseStatus)
admin.site.register(ProductDatabase)
