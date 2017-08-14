from django.conf.urls import url
from django.views.generic import ListView, DetailView
from Database_Models.models import Volunteer, Project, BenefitedInstitution

from .views import VolunteerCreatView, ProjectCreatView, BenefitedCreatView

# The "object" reference will give a warning. But it's fine.
urlpatterns = [
    # Volunteer
    url(r'^volunteer/$', ListView.as_view(queryset=Volunteer.objects.all().order_by("-first_name")[:25],
                                          template_name="volunteer/volunteer_list.html")),
    url(r'^volunteer/(?P<pk>\d+)$', DetailView.as_view(model=Volunteer,
                                             template_name='volunteer/volunteer_detail.html')),
    url(r'^volunteer/new_volunteer/$', VolunteerCreatView.as_view(), name='new-volunteer'),

    # Project
    url(r'^project/$', ListView.as_view(queryset=Project.objects.all().order_by("-name")[:25],
                                        template_name="project/project_list.html")),
    url(r'^project/(?P<pk>\d+)$', DetailView.as_view(model=Project,
                                             template_name='project/project_detail.html')),
    url(r'^project/new_project/$', ProjectCreatView.as_view(), name='new-project'),

    # Benefited Instituition
    url(r'^benefited/$', ListView.as_view(queryset=BenefitedInstitution.objects.all().order_by("-name")[:25],
                                        template_name="benefited/benefited_list.html")),
    url(r'^benefited/(?P<pk>\d+)$', DetailView.as_view(model=BenefitedInstitution,
                                             template_name='benefited/benefited_detail.html')),
    url(r'^benefited/new_benefited/$', BenefitedCreatView.as_view(), name='new-benefited'),

]
