# from django.http import Http404  # HttpResponse,
from django.shortcuts import render  # redirect
# import datetime as dt
from .models import Project


# Create your views here.
def home(request):
    projects = Project.project_item()
    # title = "Sami-Mai Portfolio"
    return render(request, 'index.html', {"projects": projects})


def project(request, slug):
    # project = self.project
    project = Project.objects.get(slug=slug)

    return render(request, 'all_projects/project.html', {"project": project})
