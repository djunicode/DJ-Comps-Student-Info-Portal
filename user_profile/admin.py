from django.contrib import admin
# from .models import TeacherProfile, Experience
from .models import Hackathon, Committee, ResearchPaper, BeProject, Internship
from .models import Project, StudentProfile, Skill

# Register your models here.
# admin.site.register(TeacherProfile)
# admin.site.register(Experience)
admin.site.register(StudentProfile)
admin.site.register(Internship)
admin.site.register(Project)
admin.site.register(Hackathon)
admin.site.register(Committee)
admin.site.register(ResearchPaper)
admin.site.register(BeProject)
admin.site.register(Skill)
