from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from squashapp.models import ProjectDatabase
from squashapp.serializers import SquashappSerializer
from rest_framework import generics
# Create your views here.


# VIEWING THE HOME PAGE REQUIRES THE USER TO LOGIN FIRST
# IF THE USER IS NOT LOGGED IN, HE WILL BE REDIRECTED TO THE LOGIN_URL
# SETTING IN SETTING.PY FILE I.E THE /accounts/login page
# THIS IS THE USE OF THE @login_required DECORATOR
@login_required
def home(request):
    projects = ProjectDatabase.objects.all()
    context = {'projects':projects}
    return render(request,'home.html', context)


class ProjectList(generics.ListCreateAPIView):
    queryset = ProjectDatabase.objects.all()
    serializer_class = SquashappSerializer

class ProjectDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectDatabase.objects.all()
    serializer_class =  SquashappSerializer
