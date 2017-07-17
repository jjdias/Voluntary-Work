from django.db import models

# Phone validator. Link at the end.
from django.core.validators import RegexValidator

# Create your models here.


# This is the first part.

# I'm developing this for, mostly, Algarve University. That will explain some of the model choices.
class University(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

# Since this is being developed for a university we will have a campus class.
# A university may have multiple campus but I'm going with the idea that a campus has only one university.
class Campus(models.Model):
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# A campus has multiple fields of sutdy while another campus, from the same university, has other field.
# I think it's a bit redundant but thats how they do it in there.
class Field_of_study(models.Model):  # Or "Unidade Organica"
    name = models.CharField(max_length=140)
    abbreviation = models.CharField(max_length=5)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        # return "%s, %s" % (self.abbreviation, self.name)

# And a course. The fruit on a, not entirely sure why, long tree.
class Course(models.Model):
    name = models.CharField(max_length=140)
    abbreviation = models.CharField(max_length=5)
    field_of_study = models.ForeignKey(Field_of_study, on_delete=models.CASCADE)

    def __str__(self):
        # return self.name
        return "%s, %s" % (self.abbreviation, self.name)

# An finally the volunteer.
class Volunteer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_birth = models.DateField()
    email = models.EmailField()

    # For verifying the phone.
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list

    # TODO Should this be allowed to be NULL or not.
    # Now there is a problem here. Employee can be volunteers and no have a course. Not sure whats teh best solution yet.
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        # return self.name
        return "%s, %s" % (self.last_name, self.first_name)


# Second part

# A project can have multiple dates and vise-versa.
class Date_Project(models.Model):
    # This would be the ideal but I'm not sure on how to do it.
    # date_begins = models.DateTimeField()
    # date_ends = models.DateTimeField()
    # TODO fix the beginning and ending of projects

    date_begins = models.DateTimeField()

    # TODO make the other way around on the project date thing.
    # project = models.ManyToManyField(Project)
    # project = models.ForeignKey('models.Project')

    def __str__(self):
        return str(self.date_begins)

class Project(models.Model):
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140)
    description = models.TextField()

    date_project_begins = models.ManyToManyField(Date_Project)

    def __str__(self):
        return self.name



# Phone verification: https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models