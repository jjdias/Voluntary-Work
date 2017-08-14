from django import forms
from django.forms import DateTimeField, DateInput, ModelMultipleChoiceField
from django.forms.widgets import DateTimeInput, SelectMultiple

from .models import Volunteer, Project, BenefitedInstitution

class VolunteerCreateForm(forms.ModelForm):
    class Meta:
        model = Volunteer



        widgets = {
            'date_birth': DateInput(attrs={'type': 'date'}),
        }

        # fields = '__all__'
        fields = [
            'first_name',
            'last_name',
            'date_birth',
            'email',
            'phone_number',
            'course',
            'projects_participating',
        ]

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project

        # Stll have no idea whats up with this.
        # pattern="[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}"
        widgets = {
            'date_time': DateTimeInput(attrs={'type': 'datetime-local', 'pattern': '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}'}),
            # 'volunteers_participating': SelectMultiple()
        }

        fields = [
            'name',
            'address',
            'description',
            'date_time',
            'volunteers_participating',
            'institution_benefited',
        ]

class BenefitedCreateForm(forms.ModelForm):
    class Meta:
        model = BenefitedInstitution
        fields = [
            'name',
            'address',
            'representative_name',
            'area_of_work',
            'contact',
        ]