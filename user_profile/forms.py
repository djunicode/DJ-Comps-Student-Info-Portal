from django import forms
from django.forms import ModelForm
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from .models import StudentProfile, Hackathon, Education, KT, Skill, Internship, Project, Committee, BeProject, ResearchPaper


class LoginForm(forms.Form):
    Sap_Id = forms.IntegerField(
        validators=[MaxValueValidator(99999999999),
                    MinValueValidator(10000000000)])
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.Form):
    Sap_Id = forms.IntegerField(
        validators=[MaxValueValidator(99999999999),
                    MinValueValidator(10000000000)])
    Email_Id = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['student', 'Sap_Id', 'department', 'photo', 'github_id', 'bio', 'gender', 'mobileNo', 'year']

class HackathonForm(forms.ModelForm):
    class Meta:
        model = Hackathon
        fields = ['CompetitionName', 'Date', 'Desc', 'URL', 'image1', 'image2', 'image3', 'image4', 'image5']

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = ['company', 'Position', 'Loc', 'From', 'To', 'desc', 'Certificate', 'image1', 'image2', 'image3', 'image4', 'image5']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['sem1_gpa', 'sem2_gpa', 'sem3_gpa', 'sem4_gpa', 'sem4_gpa', 'sem5_gpa', 'sem6_gpa', 'sem7_gpa', 'sem8_gpa']

class KTForm(forms.ModelForm):
    class Meta:
        model = KT
        fields = ['subject_name', 'subject_semester']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['skill']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['ProjName', 'ProjDesc', 'ProjURL', 'projectUnderTeacher']

class CommitteeForm(forms.ModelForm):
    class Meta:
        model = Committee
        fields = ['OrganisationName', 'YourPosition', 'Loc', 'dateFrom', 'dateTo', 'Desc', 'Certificate', 'image1', 'image2', 'image3', 'image4', 'image5']

class ResearchPaperForm(forms.ModelForm):
    class Meta:
        model = ResearchPaper
        fields = ['Title', 'Publication', 'DateOfPublication', 'Desc', 'LinkToPaper', 'PaperId', 'image1', 'image2', 'image3', 'image4', 'image5']

class BeProjectForm(forms.ModelForm):
    class Meta:
        model = BeProject
        fields = ['ProjName', 'ProjDesc', 'ProjURL', 'image1', 'image2', 'image3', 'image4', 'image5']

