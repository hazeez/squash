from django.forms import widgets
from rest_framework import serializers
from squashapp.models import ProjectDatabase, ProjectReviewDetails

class AllProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDatabase
        fields = ('project_release_name','project_uid','project_customer_name',
                  'project_class','project_products','project_base_version',
                  'project_total_effort','project_base_effort','project_cut_effort',
                  'project_testing_effort','project_cob_effort','project_status',
                  'project_manager','project_backup_manager','project_managed_by',
                  'project_primary_sqa','project_secondary_sqa','project_tertiary_sqa',
                  'project_region_lead','project_region','project_subregion',
                  'project_methodology','project_created_date','project_updated_date',
                  'project_start_date','project_end_date','project_duration',
                  'project_description','project_scm_tool','project_scm_path',
                  'project_soft_path','project_bug_tool','project_released_date',
                  'project_release_status')

class ReleaseDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectReviewDetails


class ProjectReleaseInfoSerializer(serializers.ModelSerializer):
    # Refer to nested relationships in http://www.django-rest-framework.org/api-guide/relations/
    # the project_details variable should match with the name provided in
    # models.py file foreign key "related_name"
    project_details = ReleaseDetailsSerializer(many=True)

    class Meta:
        model = ProjectDatabase
        fields = ('project_release_name','project_uid','project_customer_name',
                  'project_class','project_products','project_base_version',
                  'project_total_effort','project_base_effort','project_cut_effort',
                  'project_testing_effort','project_cob_effort','project_status',
                  'project_manager','project_backup_manager','project_managed_by',
                  'project_primary_sqa','project_secondary_sqa','project_tertiary_sqa',
                  'project_region_lead','project_region','project_subregion',
                  'project_methodology','project_created_date','project_updated_date',
                  'project_start_date','project_end_date','project_duration',
                  'project_description','project_scm_tool','project_scm_path',
                  'project_soft_path','project_bug_tool','project_released_date',
                  'project_release_status','project_details')



