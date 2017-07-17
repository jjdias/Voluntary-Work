from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from database_models.models import Volunteer

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Volunteer.objects.all().order_by("-name")[:25],
                                    template_name="volunteer/list.html")),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Volunteer,
                                    template_name='volunteer/volunteer.html')),
]
