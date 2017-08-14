from django.shortcuts import render
from django.views.generic import CreateView
from .forms import VolunteerCreateForm, ProjectCreateForm, BenefitedCreateForm

# Create your views here.

class VolunteerCreatView(CreateView):
    form_class = VolunteerCreateForm
    template_name = 'volunteer/volunteer_form.html'
    success_url = "/list/volunteer_list/"

class ProjectCreatView(CreateView):
    form_class = ProjectCreateForm
    template_name = 'project/project_form.html'
    success_url = "/list/project_list/"

class BenefitedCreatView(CreateView):
    form_class = BenefitedCreateForm
    template_name = 'benefited/benefited_form.html'
    success_url = "/list/benefited_list/"