from django.forms import widgets
from rest_framework import serializers
from squashapp.models import ProjectDatabase

class SquashappSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDatabase
        fields = ('project_release_name','project_uid','project_class',
                  'project_primary_sqa', 'project_region','project_start_date',
                    'project_end_date','project_duration')


