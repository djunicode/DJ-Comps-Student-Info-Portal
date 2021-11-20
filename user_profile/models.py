from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db.models.base import Model
from django.db.models.deletion import SET_NULL
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from simple_history.models import HistoricalRecords
from django.contrib.postgres.fields import JSONField

# import django_filters


class TeacherProfile(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    Sap_Id = models.BigIntegerField(
        validators=[MaxValueValidator(99999999999), MinValueValidator(10000000000)],
        blank=True,
        null=True,
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    photo = models.FileField(blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, blank=True, null=True
    )

    class Meta:
        permissions = (("view_teacher", "Can see teacher profile"),)

    def __str__(self):
        return str(self.Sap_Id)


class StudentProfile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name="stud")
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    Sap_Id = models.BigIntegerField(
        validators=[MaxValueValidator(99999999999), MinValueValidator(10000000000)],
        blank=True,
        null=True,
    )
    sap = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    mentor = models.ForeignKey(
        TeacherProfile, on_delete=SET_NULL, blank=True, null=True
    )
    photo = models.FileField(blank=True, null=True)
    github_id = models.URLField(null=True, blank=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(
        max_length=6, choices=GENDER_CHOICES, blank=True, null=True
    )
    mobileNo = models.CharField(max_length=50, blank=True, null=True)
    YEAR_CHOICES = (
        ("FE", "First Year"),
        ("SE", "Second Year"),
        ("TE", "Third Year"),
        ("BE", "Final Year"),
    )
    year = models.CharField(max_length=20, choices=YEAR_CHOICES, blank=True, null=True)

    class Meta:
        permissions = (("view_student", "Can see student profile"),)

    def __str__(self):
        return str(str(self.Sap_Id) + "   " + str(self.id))


class Recruiter(models.Model):
    recruiter = models.OneToOneField(User, on_delete=models.CASCADE)


class Subject(models.Model):
    SEM_CHOICES = (
        ("SEM1", "Semester 1"),
        ("SEM2", "Semester 2"),
        ("SEM3", "Semester 3"),
        ("SEM4", "Semester 4"),
        ("SEM5", "Semester 5"),
        ("SEM6", "Semester 6"),
        ("SEM7", "Semester 7"),
        ("SEM8", "Semester 8"),
    )
    name = models.CharField(max_length=100)
    sem = models.CharField(max_length=20, choices=SEM_CHOICES)

    def __str__(self):
        return str(self.sem) + str(self.name)


class TermTest(models.Model):
    tt_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.tt_name)


class SubjectMarks(models.Model):
    tt = models.ForeignKey(TermTest, related_name="subject", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MaxValueValidator(0), MinValueValidator(20)],
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.tt.tt_name) + str(self.subject)


class Education(models.Model):
    student_profile = models.OneToOneField(
        StudentProfile, related_name="education", on_delete=models.CASCADE
    )
    sem1_gpa = models.FloatField(blank=True, null=True, default=None)
    sem1_marksheet = models.FileField(blank=True, null=True)
    sem2_gpa = models.FloatField(blank=True, null=True, default=None)
    sem2_marksheet = models.FileField(blank=True, null=True)
    sem3_gpa = models.FloatField(blank=True, null=True, default=None)
    sem3_marksheet = models.FileField(blank=True, null=True)
    sem4_gpa = models.FloatField(blank=True, null=True, default=None)
    sem4_marksheet = models.FileField(blank=True, null=True)
    sem5_gpa = models.FloatField(blank=True, null=True, default=None)
    sem5_marksheet = models.FileField(blank=True, null=True)
    sem6_gpa = models.FloatField(blank=True, null=True, default=None)
    sem6_marksheet = models.FileField(blank=True, null=True)
    sem7_gpa = models.FloatField(blank=True, null=True, default=None)
    sem7_marksheet = models.FileField(blank=True, null=True)
    sem8_gpa = models.FloatField(blank=True, null=True, default=None)
    sem8_marksheet = models.FileField(blank=True, null=True)
    history = HistoricalRecords()


class KT(models.Model):
    subject_name = models.CharField(max_length=100)
    SEM_CHOICES = (
        ("SEM1", "Semester 1"),
        ("SEM2", "Semester 2"),
        ("SEM3", "Semester 3"),
        ("SEM4", "Semester 4"),
        ("SEM5", "Semester 5"),
        ("SEM6", "Semester 6"),
        ("SEM7", "Semester 7"),
        ("SEM8", "Semester 8"),
    )
    subject_semester = models.CharField(max_length=20, choices=SEM_CHOICES)
    education = models.ForeignKey(
        Education, related_name="kt", on_delete=models.CASCADE
    )


"""
class Experience(models.Model):
    employee = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=50)
    yourPosition = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date = models.DateField(("Date"), default=datetime.date.today, blank=True)
"""


class Image(models.Model):
    image = models.ImageField(upload_to="images/", null=False, blank=False)


class Hackathon(models.Model):
    student_profile = models.ForeignKey(
        StudentProfile, related_name="hackathon", on_delete=models.CASCADE
    )
    CompetitionName = models.CharField(max_length=50, blank=True, null=True)
    StartDate = models.DateField(("StartDate"), default=datetime.date.today)
    EndDate = models.DateField(("EndDate"), default=datetime.date.today)
    Desc = models.TextField(blank=True, null=True)
    URL = models.URLField(null=True, blank=True)  # if hosted url
    Github_url = models.URLField(null=True, blank=True)
    Certificate = models.FileField(blank=True, null=True)
    image1 = models.FileField(null=True, blank=True)
    image2 = models.FileField(null=True, blank=True)
    # image4 = models.FileField(null=True, blank=True)
    # image5 = models.FileField(null=True, blank=True)
    history = HistoricalRecords()
    is_approved = models.BooleanField(null=True, blank=True, default=None)
    total_no_of_hours = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.CompetitionName)


class Skill(models.Model):
    user_profile = models.ForeignKey(
        StudentProfile, related_name="skill", on_delete=models.CASCADE
    )
    skill = models.CharField(max_length=50)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.skill)


class Internship(models.Model):
    employee = models.ForeignKey(
        StudentProfile, related_name="internships", on_delete=models.CASCADE
    )
    company = models.CharField(max_length=50, blank=True, null=True)
    Position = models.CharField(max_length=50, blank=True, null=True)
    Loc = models.CharField(max_length=50, blank=True, null=True)
    From = models.DateField(("Date"), default=datetime.date.today)
    To = models.DateField(("Date"), default=datetime.date.today)
    desc = models.TextField(blank=True, null=True)
    how_options = (
        ("In College", "In College"),
        ("Out of College", "Out of College"),
    )
    how = models.CharField(max_length=16, choices=how_options, blank=True, null=True)
    stipend_options = (
        ("Paid", "Paid"),
        ("Unpaid", "Unpaid"),
    )
    stipend = models.CharField(
        max_length=6, choices=stipend_options, blank=True, null=True
    )
    offer_letter = models.FileField(blank=True, null=True)
    Certificate = models.FileField(blank=True, null=True)
    total_hours = models.IntegerField(default=0, null=True, blank=True)
    evaluation_report_self_one = models.FileField(blank=True, null=True)
    evaluation_report_self_two = models.FileField(blank=True, null=True)
    evaluation_report_self_three = models.FileField(blank=True, null=True)

    evaluation_report_mentor = models.FileField(blank=True, null=True)
    evaluation_report_supervisor = models.FileField(blank=True, null=True)
    # evaluation_report_self = models.FileField(blank=True, null=True)
    # images = models.ManyToManyField(Image)

    # image1 = models.FileField(blank=True, null=True)
    # image2 = models.FileField(blank=True, null=True)
    # image3 = models.FileField(blank=True, null=True)
    # image4 = models.FileField(blank=True, null=True)
    # image5 = models.FileField(blank=True, null=True)
    history = HistoricalRecords()
    is_approved = models.BooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.company)


class Project(models.Model):
    student_profile = models.ForeignKey(
        StudentProfile, related_name="projects", on_delete=models.CASCADE
    )
    ProjName = models.CharField(max_length=50, blank=True, null=True)
    ProjURL = models.URLField(blank=True, null=True)
    ProjDesc = models.TextField(blank=True, null=True)
    projectUnderTeacher = models.ForeignKey(
        TeacherProfile,
        blank=True,
        related_name="verifiedprojects",
        null=True,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        Skill,
        related_name="projectskills",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    # images = models.ManyToManyField(Image)

    image1 = models.FileField(blank=True, null=True)
    image2 = models.FileField(
        blank=True,
        null=True,
    )

    history = HistoricalRecords()
    is_approved = models.BooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.ProjName)


class Committee(models.Model):
    employee = models.ForeignKey(
        StudentProfile, related_name="committee", on_delete=models.CASCADE
    )
    OrganisationName = models.CharField(max_length=50, blank=True, null=True)
    YourPosition = models.CharField(max_length=50, blank=True, null=True)
    # Loc = models.CharField(max_length=50, blank=True, null=True)
    dateFrom = models.DateField(("Date"), default=datetime.date.today)
    dateTo = models.DateField(("Date"), default=datetime.date.today)
    Desc = models.TextField(blank=True, null=True)
    Certificate = models.FileField(null=True, blank=True)
    # images = models.ManyToManyField(Image)

    # image1 = models.FileField(blank=True, null=True)
    # image2 = models.FileField(null=True, blank=True)
    # image3 = models.FileField(null=True, blank=True)
    # image4 = models.FileField(null=True, blank=True)
    # image5 = models.FileField(null=True, blank=True)
    history = HistoricalRecords()
    is_approved = models.BooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.OrganisationName)


class ResearchPaper(models.Model):
    student = models.ForeignKey(
        StudentProfile, related_name="researchpaper", on_delete=models.CASCADE
    )
    Title = models.CharField(max_length=255, null=True, blank=True)
    Publication = models.CharField(max_length=255, null=True, blank=True)  #
    DateOfPublication = models.DateField(("Date"), default=datetime.date.today)
    Desc = models.TextField(null=True, blank=True)
    LinkToPaper = models.URLField(blank=True, null=True)
    PaperId = models.CharField(max_length=50, null=True, blank=True)  #
    isbn = models.CharField(max_length=50, null=True, blank=True)
    issn = models.CharField(max_length=50, null=True, blank=True)  #
    proof_of_submission = models.FileField(null=True, blank=True)  #
    project_mentor = models.CharField(max_length=100, null=True, blank=True)  #
    duration_of_project = models.CharField(max_length=100, null=True, blank=True)  #
    total_hours = models.IntegerField(default=0, null=True, blank=True)  #
    research_type = (
        ("Conference", "Conference"),
        ("Journal", "Journal"),
        ("Chapter", "Chapter"),
    )
    type = models.CharField(max_length=20, choices=research_type, blank=True, null=True)
    research_impact_factor = models.FloatField(blank=True, null=True, default=0)
    indexing = models.CharField(max_length=255, blank=True, null=True)
    # images = models.ManyToManyField(Image)

    # image1 = models.FileField(null=True, blank=True)
    # image2 = models.FileField(null=True, blank=True)
    # image3 = models.FileField(null=True, blank=True)
    # image4 = models.FileField(null=True, blank=True)
    # image5 = models.FileField(null=True, blank=True)
    history = HistoricalRecords()
    is_approved = models.BooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.Title)


class BeProject(models.Model):
    student = models.ForeignKey(
        StudentProfile, related_name="beprojects", on_delete=models.CASCADE
    )
    ProjName = models.CharField(max_length=50, null=True, blank=True)
    ProjURL = models.URLField(null=True, blank=True)
    ProjDesc = models.CharField(max_length=500, null=True, blank=True)
    teammates = models.ManyToManyField(
        StudentProfile, related_name="beteammate", blank=True
    )
    projectUnderTeacher = models.ForeignKey(
        TeacherProfile,
        blank=True,
        null=True,
        related_name="verifiedbeprojects",
        on_delete=models.CASCADE,
    )
    # images = models.ManyToManyField(Image)

    image1 = models.FileField(null=True, blank=True)
    image2 = models.FileField(null=True, blank=True)
    # image3 = models.FileField(null=True, blank=True)
    # image4 = models.FileField(null=True, blank=True)
    # image5 = models.FileField(null=True, blank=True)
    project_report = models.FileField(null=True, blank=True)
    history = HistoricalRecords()
    is_approved = models.BooleanField(null=True, blank=True, default=None)

    def __str__(self):
        return str(self.ProjName)


class ExtraCurricular(models.Model):
    extra_curricular_type = (
        ("Coursera", "Coursera"),
        ("NPTEL", "NPTEL"),
        ("Sports", "Sports"),
        ("Others", "Others"),
    )
    student = models.ForeignKey(
        StudentProfile, related_name="extracurricular", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    desc = models.CharField(max_length=500, null=True, blank=True)
    achievements = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(("Date"), default=datetime.date.today)
    Certificate = models.FileField(null=True, blank=True)
    extra_curricular_type = models.CharField(max_length=20, choices=extra_curricular_type, blank=True, null=True)

    # images = models.ManyToManyField(Image)

    # image1 = models.FileField(null=True, blank=True)
    # image2 = models.FileField(null=True, blank=True)
    # image3 = models.FileField(null=True, blank=True)
    # image4 = models.FileField(null=True, blank=True)
    # image5 = models.FileField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.name)


class CompetitiveExams(models.Model):
    student = models.OneToOneField(
        StudentProfile, related_name="competitiveexams", on_delete=models.CASCADE
    )
    gre_score = models.CharField(max_length=10, null=True, blank=True)
    toefl_score = models.CharField(max_length=10, null=True, blank=True)
    cat_score = models.CharField(max_length=10, null=True, blank=True)
    gate_score = models.CharField(max_length=10, null=True, blank=True)
    gmat_score = models.CharField(max_length=10, null=True, blank=True)
    is_approved = models.BooleanField(null=True, blank=True, default=None)
    # mhcet_score = models.CharField(max_length=10, null=True, blank=True)


class Admit(models.Model):
    student = models.ForeignKey(
        StudentProfile, related_name="admit", on_delete=models.CASCADE
    )
    college_name = models.CharField(max_length=50, null=True, blank=True)
    masters_field = models.CharField(max_length=50, null=True, blank=True)
    college_location = models.CharField(max_length=50, null=True, blank=True)
    selected = models.CharField(max_length=50, null=True, blank=True)
    admit_proof = models.FileField(blank=True, null=True)
    is_approved = models.BooleanField(null=True, blank=True, default=None)

class Placements(models.Model):
    student = models.ForeignKey(
        StudentProfile, related_name="placement", on_delete=models.CASCADE
    )
    company_name = models.CharField(max_length=255, blank=False, null=False)
    offer_letter = models.FileField(null=True)
    is_approved = models.BooleanField(null=True, blank=True, default=None)
