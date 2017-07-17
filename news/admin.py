from django.contrib import admin
from news.models import Post
# Register your models here.

# Adding the news post feature to the admin page.
admin.site.register(Post)
