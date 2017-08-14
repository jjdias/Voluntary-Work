from django.conf.urls import url, include
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .forms import PostCreateForm
from .models import Post

# Create your views here.

# Easy way.
# def post_create_view(request):
#     form = PostCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/news/")
#     if form.errors:
#         print(form.errors)
#
#     template_name = 'news/post_form.html'
#     context = {"form": form}
#     return render(request, template_name, context)

# Easier way.
class PostCreateView(CreateView):
    form_class = PostCreateForm
    template_name = 'news/post_form.html'
    success_url = "/news/"