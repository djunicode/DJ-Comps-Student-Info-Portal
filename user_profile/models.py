from django.db import models
import datetime
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from django.db.models.signals import post_save
from django.core.validators import URLValidator


# class TeacherProfile(models.Model):
#     user = models.OneToOneField(User)
#     teacherId = models.CharField(max_length=15)
#     department = models.CharField(max_length=50)
#     photo = models.FileField(blank=True)
#     bio = models.CharField(max_length=200)
#     GENDER_CHOICES = (
#         ("Male", "Male"),
#         ("Female", "Female"),
#     )
#     gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
#
#
# def create_profile(sender, **kwargs):
#     user = kwargs["instance"]
#     if kwargs["created"]:
#         user_profile = TeacherProfile(user=user)
#         user_profile.save()
#
#
# post_save.connect(create_profile, sender=User)
#
#
# class Experience(models.Model):
#     employee = models.ForeignKey(TeacherProfile)
#     companyName = models.CharField(max_length=50)
#     yourPosition = models.CharField(max_length=50)
#     Location = models.CharField(max_length=50)
#     description = models.CharField(max_length=500)
#     date = models.DateField(("Date"), default=datetime.date.today, blank=True)


class Hackathon(models.Model):
    CompetitionName = models.CharField(max_length=50)
    Date = models.DateField()
    Desc = models.CharField(max_length=500)
    URL = models.TextField(validators=[URLValidator()])
    isVerified = models.BooleanField(default=False)
# verifiedBy = models.ForeignKey(TeacherProfile)


class Skill(models.Model):
    skill = models.CharField(max_length=50)


class StudentProfile(AbstractUser):
    Sap_Id = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    photo = models.FileField(blank=True)
    bio = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    mobileNo = models.CharField(max_length=50)
    YEAR_CHOICES = (
        ("FE", "First Year"),
        ("SE", "Second Year"),
        ("TE", "Third Year"),
        ("BE", "Final Year"),
    )
    year = models.CharField(max_length=20, choices=YEAR_CHOICES)
    skills = models.ManyToManyField(Skill, blank=True)
    hackathon = models.ManyToManyField(Hackathon, blank=True)


class Internship(models.Model):
    employee = models.ForeignKey(StudentProfile)
    company = models.CharField(max_length=50, blank=True)
    Position = models.CharField(max_length=50, blank=True)
    Loc = models.CharField(max_length=50, blank=True)
    From = models.DateField(("Date"), default=datetime.date.today, blank=True)
    To = models.DateField(("Date"), default=datetime.date.today, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    Certificate = models.FileField(blank=True)
    isVerified = models.BooleanField(default=False)
# verifiedBy = models.ForeignKey(TeacherProfile)


class Project(models.Model):
    student = models.ForeignKey(StudentProfile)
    ProjName = models.CharField(max_length=50)
    ProjURL = models.TextField(validators=[URLValidator()], blank=True)
    ProjDesc = models.CharField(max_length=500, blank=True)
    isVerified = models.BooleanField(default=False)
# verifiedBy = models.ForeignKey(TeacherProfile)
# projectUnderTeacher = models.ForeignKey(TeacherProfile)


class Committee(models.Model):
    employee = models.ForeignKey(StudentProfile)
    OrganisationName = models.CharField(max_length=50)
    YourPosition = models.CharField(max_length=50)
    Loc = models.CharField(max_length=50, blank=True)
    dateFrom = models.DateField(("Date"), default=datetime.date.today, blank=True)
    dateTo = models.DateField(("Date"), default=datetime.date.today, blank=True)
    Desc = models.CharField(max_length=500, blank=True)
    Certificate = models.FileField(blank=True)
    isVerified = models.BooleanField(default=False)
# verifiedBy = models.ForeignKey(TeacherProfile)


class ResearchPaper(models.Model):
    student = models.ForeignKey(StudentProfile)
    Title = models.CharField(max_length=50)
    Publication = models.CharField(max_length=100)
    DateOfPublication = models.DateField(("Date"), default=datetime.date.today, blank=True)
    Desc = models.CharField(max_length=500, blank=True)
    LinkToPaper = models.TextField(validators=[URLValidator()], blank=True)
    PaperId = models.CharField(max_length=50, blank=True)
# Published_under = models.ForeignKey(TeacherProfile)


class BeProject(models.Model):
    student = models.ForeignKey(StudentProfile, related_name='BE_projects')
    ProjName = models.CharField(max_length=50)
    ProjURL = models.TextField(validators=[URLValidator()])
    ProjDesc = models.CharField(max_length=500, blank=True)
    isVerified = models.BooleanField(default=False)
    teammates = models.ManyToManyField(StudentProfile, related_name='BE_teammate', blank=True)
# verifiedBy = models.ForeignKey(TeacherProfile)
# projectUnderTeacher = models.ForeignKey(TeacherProfile)
