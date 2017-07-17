from django.contrib import admin
from database_models.models import University, Campus, Field_of_study, Course, Volunteer, Date_Project, Project

# Register your models here.

admin.site.register(University)
admin.site.register(Campus)
admin.site.register(Field_of_study)
admin.site.register(Course)
admin.site.register(Volunteer)

admin.site.register(Date_Project)
admin.site.register(Project)
