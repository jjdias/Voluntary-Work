from django.conf.urls import url
from django.views.generic import ListView, DetailView
from database_models.models import Volunteer, Project, BenefitedInstitution

# The "object" reference will give a warning. But it's fine.
urlpatterns = [
    # Volunteer
    url(r'^volunteer/$', ListView.as_view(queryset=Volunteer.objects.all().order_by("-first_name")[:25],
                                          template_name="volunteer/list.html")),
    url(r'^volunteer/(?P<pk>\d+)$', DetailView.as_view(model=Volunteer,
                                             template_name='volunteer/volunteer.html')),

    # Project
    url(r'^project/$', ListView.as_view(queryset=Project.objects.all().order_by("-name")[:25],
                                        template_name="project/list.html")),
    url(r'^project/(?P<pk>\d+)$', DetailView.as_view(model=Project,
                                             template_name='project/project.html')),

    # Benefited Instituition
    url(r'^benefited/$', ListView.as_view(queryset=BenefitedInstitution.objects.all().order_by("-name")[:25],
                                        template_name="benefited/list.html")),
    url(r'^benefited/(?P<pk>\d+)$', DetailView.as_view(model=BenefitedInstitution,
                                             template_name='benefited/benefited.html')),
]
