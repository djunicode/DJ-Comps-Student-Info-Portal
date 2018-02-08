from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords


class Recruiter(models.Model):
    recruiter = models.OneToOneField(User, on_delete=models.CASCADE)


class TeacherProfile(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    Sap_Id = models.BigIntegerField(validators=[MaxValueValidator(99999999999), MinValueValidator(10000000000)])
    department = models.CharField(max_length=50)
    photo = models.FileField(blank=True)
    bio = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    class Meta:
        permissions = (
            ("view_teacher", "Can see teacher profile"),
        )

    def __str__(self):
        return str(self.Sap_Id)


class Experience(models.Model):
    employee = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50)
    yourPosition = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date = models.DateField(("Date"), default=datetime.date.today, blank=True)


class Hackathon(models.Model):
    CompetitionName = models.CharField(max_length=50)
    Date = models.DateField()
    Desc = models.CharField(max_length=500)
    URL = models.TextField(validators=[URLValidator()])
    image1 = models.FileField()
    image2 = models.FileField(blank=True)
    image3 = models.FileField(blank=True)
    image4 = models.FileField(blank=True)
    image5 = models.FileField(blank=True)
    history = HistoricalRecords()


class Skill(models.Model):
    skill = models.CharField(max_length=50)
    history = HistoricalRecords()


class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    Sap_Id = models.BigIntegerField(validators=[MaxValueValidator(99999999999), MinValueValidator(10000000000)])
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

    class Meta:
        permissions = (
            ("view_student", "Can see student profile"),
        )

    def __str__(self):
        return str(self.Sap_Id)


class Internship(models.Model):
    employee = models.ForeignKey(StudentProfile, related_name="internships")
    company = models.CharField(max_length=50, blank=True)
    Position = models.CharField(max_length=50, blank=True)
    Loc = models.CharField(max_length=50, blank=True)
    From = models.DateField(("Date"), default=datetime.date.today, blank=True)
    To = models.DateField(("Date"), default=datetime.date.today, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    Certificate = models.FileField(blank=True)
    image1 = models.FileField()
    image2 = models.FileField(blank=True)
    image3 = models.FileField(blank=True)
    image4 = models.FileField(blank=True)
    image5 = models.FileField(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.company)


class Project(models.Model):
    student = models.ForeignKey(StudentProfile, related_name="projects")
    ProjName = models.CharField(max_length=50)
    ProjURL = models.TextField(validators=[URLValidator()], blank=True)
    ProjDesc = models.CharField(max_length=500, blank=True)
    projectUnderTeacher = models.ForeignKey(TeacherProfile, blank=True, null=True, related_name="verifiedprojects")
    image1 = models.FileField()
    image2 = models.FileField(blank=True)
    image3 = models.FileField(blank=True)
    image4 = models.FileField(blank=True)
    image5 = models.FileField(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.ProjName)


class Committee(models.Model):
    employee = models.ForeignKey(StudentProfile, related_name="committee")
    OrganisationName = models.CharField(max_length=50)
    YourPosition = models.CharField(max_length=50)
    Loc = models.CharField(max_length=50, blank=True)
    dateFrom = models.DateField(("Date"), default=datetime.date.today, blank=True)
    dateTo = models.DateField(("Date"), default=datetime.date.today, blank=True)
    Desc = models.CharField(max_length=500, blank=True)
    Certificate = models.FileField(blank=True)
    image1 = models.FileField()
    image2 = models.FileField(blank=True)
    image3 = models.FileField(blank=True)
    image4 = models.FileField(blank=True)
    image5 = models.FileField(blank=True)
    history = HistoricalRecords()


class ResearchPaper(models.Model):
    student = models.ForeignKey(StudentProfile, related_name="researchpaper")
    Title = models.CharField(max_length=50)
    Publication = models.CharField(max_length=100)
    DateOfPublication = models.DateField(("Date"), default=datetime.date.today, blank=True)
    Desc = models.CharField(max_length=500, blank=True)
    LinkToPaper = models.TextField(validators=[URLValidator()], blank=True)
    PaperId = models.CharField(max_length=50, blank=True)
    Published_under = models.ForeignKey(TeacherProfile, blank=True, null=True, related_name="verifiedpaper")
    image1 = models.FileField()
    image2 = models.FileField(blank=True)
    image3 = models.FileField(blank=True)
    image4 = models.FileField(blank=True)
    image5 = models.FileField(blank=True)
    history = HistoricalRecords()


class BeProject(models.Model):
    student = models.ForeignKey(StudentProfile, related_name='beprojects')
    ProjName = models.CharField(max_length=50)
    ProjURL = models.TextField(validators=[URLValidator()])
    ProjDesc = models.CharField(max_length=500, blank=True)
    teammates = models.ManyToManyField(StudentProfile, related_name='beteammate', blank=True)
    projectUnderTeacher = models.ForeignKey(TeacherProfile, blank=True, null=True, related_name="verifiedbeprojects")
    image1 = models.FileField()
    image2 = models.FileField(blank=True)
    image3 = models.FileField(blank=True)
    image4 = models.FileField(blank=True)
    image5 = models.FileField(blank=True)
    history = HistoricalRecords()
