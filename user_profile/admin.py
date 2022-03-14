from django.contrib import admin
from .models import TeacherProfile
from .models import Hackathon, Committee, ResearchPaper, BeProject, Internship
from .models import Project, StudentProfile, Skill, Recruiter, KT, Subject
from .models import Education, ExtraCurricular, TermTest, SubjectMarks, CompetitiveExams, Admit, Image, Placements
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Image)
admin.site.register(Recruiter)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)
admin.site.register(Hackathon, SimpleHistoryAdmin)
admin.site.register(Committee, SimpleHistoryAdmin)
admin.site.register(ResearchPaper, SimpleHistoryAdmin)
admin.site.register(BeProject, SimpleHistoryAdmin)
admin.site.register(Skill, SimpleHistoryAdmin)
admin.site.register(Internship, SimpleHistoryAdmin)
admin.site.register(Project, SimpleHistoryAdmin)
admin.site.register(Education)
admin.site.register(ExtraCurricular)
admin.site.register(KT)
admin.site.register(TermTest)
admin.site.register(Subject)
admin.site.register(SubjectMarks)
admin.site.register(CompetitiveExams)
admin.site.register(Admit)
admin.site.register(Placements)
