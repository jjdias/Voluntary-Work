from django.conf.urls import url
from django.views.generic import ListView, DetailView,TemplateView

from .models import Post
from News_Blog.views import PostCreateView

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                template_name="news/post_list.html")),

    # Easy way.
    # url(r'^new_post/$', post_create_view),
    # Easier way.
    url(r'^new_post/$', PostCreateView.as_view(), name='new-post'),

    # Making the individual post pages
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
                                    template_name='news/post_detail.html')),
    # P > Named capturing Group. https://docs.djangoproject.com/en/1.11/topics/http/urls/#named-groups
    # The <pk> is seting the "Primary /key"
    # "d" Digit. "+" matches one or more digits.
    # This way the URL will be something like "news/"Int Number/".
]
