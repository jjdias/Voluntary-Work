from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from news.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="news/news.html")),

    # Making the individual post pages
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post,
                                    template_name='news/post.html')),
# P > Named capturing Group. https://docs.djangoproject.com/en/1.11/topics/http/urls/#named-groups
    # The <pk> is seting the "Primary /key"
    # "d" Digit. "+" matches one or more digits.
    # This way the URL will be something like "news/"Int Number/".
]
