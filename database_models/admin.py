from django.contrib import admin
from database_models.models import University, Campus, FieldOfStudy, Course, Volunteer, DateProject, Project, BenefitedInstitution, ContactInstitution

# Register your models here.

admin.site.register(University)
admin.site.register(Campus)
admin.site.register(FieldOfStudy)
admin.site.register(Course)
admin.site.register(Volunteer)

admin.site.register(DateProject)
admin.site.register(Project)

admin.site.register(BenefitedInstitution)
admin.site.register(ContactInstitution)
