from django.shortcuts import render
from datetime import datetime
# Create your views here.

from portfolio.models import Project
from resume.models import Experience, Education


def index(request):
    project = Project.objects.all()
    resu_exp = Experience.objects.all()
    resu_edu = Education.objects.all()
    return render(request, "core/index.html", {'projects': project, 'resu_exp': resu_exp,
                                               'resu_edu': resu_edu})
