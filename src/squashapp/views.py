from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from squashapp.models import ProjectDatabase, ProjectReviewDetails
from squashapp.serializers import AllProjectsSerializer, ReleaseDetailsSerializer, ProjectReleaseInfoSerializer
from rest_framework import generics
# Create your views here.


# VIEWING THE HOME PAGE REQUIRES THE USER TO LOGIN FIRST
# IF THE USER IS NOT LOGGED IN, HE WILL BE REDIRECTED TO THE LOGIN_URL
# SETTING IN SETTING.PY FILE I.E THE /accounts/login page
# THIS IS THE USE OF THE @login_required DECORATOR
@login_required
def home(request):
    return render(request,'home.html', '')

# get all the projects
class ProjectList(generics.ListAPIView):
    queryset = ProjectDatabase.objects.all().order_by('-project_end_date')
    serializer_class = AllProjectsSerializer

# get projects belonging to the user
class MyProjectsList(generics.ListAPIView): #RetrieveUpdateDestroyAPIView):
    serializer_class =  AllProjectsSerializer
    lookup_url_kwarg = "project_primary_sqa"

    def get_queryset(self):
        sqaname = self.kwargs.get(self.lookup_url_kwarg)
        queryset = ProjectDatabase.objects.filter(project_primary_sqa=sqaname).order_by('-project_end_date')
        return queryset

# get extended project details
class ReleaseDetails(generics.ListAPIView):
    serializer_class = ReleaseDetailsSerializer
    queryset = ProjectReviewDetails.objects.all()

# get extended project details for a particular release
class ReleaseSpecificDetails(generics.ListAPIView):
    serializer_class = ProjectReleaseInfoSerializer
    lookup_url_parameter = "release_name"

    def get_queryset(self):
        release = self.kwargs.get(self.lookup_url_parameter)
        queryset = ProjectDatabase.objects.filter(project_release_name=release)
        return queryset
