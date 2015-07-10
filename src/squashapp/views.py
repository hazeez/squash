from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from squashapp.models import ProjectDatabase
from squashapp.serializers import AllProjectsSerializer
from rest_framework import generics
# Create your views here.


# VIEWING THE HOME PAGE REQUIRES THE USER TO LOGIN FIRST
# IF THE USER IS NOT LOGGED IN, HE WILL BE REDIRECTED TO THE LOGIN_URL
# SETTING IN SETTING.PY FILE I.E THE /accounts/login page
# THIS IS THE USE OF THE @login_required DECORATOR
@login_required
def home(request):
    return render(request,'home.html', '')


class ProjectList(generics.ListAPIView):
    queryset = ProjectDatabase.objects.all()
    serializer_class = AllProjectsSerializer

class MyProjectsList(generics.ListCreateAPIView): #RetrieveUpdateDestroyAPIView):
    serializer_class =  AllProjectsSerializer
    lookup_url_kwarg = "project_primary_sqa"

    def get_queryset(self):
        sqaname = self.kwargs.get(self.lookup_url_kwarg)
        queryset = ProjectDatabase.objects.filter(project_primary_sqa=sqaname)
        return queryset

