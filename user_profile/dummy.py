from .models import (StudentProfile, TeacherProfile, Internship, Project, Committee, ResearchPaper, BeProject,
                     Hackathon, Skill, User, Education, KT)
import random
from datetime import datetime
import numpy as np


def fill():
    # Student profile model
    for i in range(60004150306, 60004150502):
        user = User.objects.create(username=i, password='asdasdasd')
        user.set_password('asdasdasd')
        user.save()
        u = StudentProfile.objects.create(student=user, Sap_Id=i, department='Computer', 
            bio='I am an engineer!', mobileNo='9856764671')
        if i % 2 == 0:
            u.gender = "Male"
        else:
            u.gender = "Female"
        if i % 4 == 0:
            u.year = "FE"
        elif i % 4 == 1:
            u.year = "SE"
        elif i % 4 == 2:
            u.year = "TE"
        elif i % 4 == 3:
            u.year = "BE"
        u.save()

    # TeacherProfile
    for i in range(90000000001, 90000000030):
        user = User.objects.create(username=i, password='asdasdasd')
        user.set_password('asdasdasd')
        user.save()
        u = TeacherProfile.objects.create(teacher=user, Sap_Id=i, department='Computer')
        if i % 2 == 0:
            u.gender = "Male"
        else:
            u.gender = "Female"
        u.save()

    # Recruiter model
    for i in range(0, 100):
        user = User.objects.create(username=i, password='asdasdasd')
        user.set_password('asdasdasd')
        user.save()
        u = Recruiter.objects.create(recruiter=user)
        u.save()

    users = StudentProfile.objects.all()
    users = [s for s in users]
    teachers = TeacherProfile.objects.all()
    teachers = [s for s in teachers]

    # Internship model
    for i in 'qwertyuiolkjhgfdsazxcvbnm':
        i = Internship.objects.create(employee=random.choice(users), company=i, Position='Intern', 
            Loc='Mumbai', desc='Computer Science')
        i.save()

    # Skills model
    skillz = ['HTML', 'CSS', 'JS', 'DJANGO', 'ML', 'NLP']
    for i in skillz:
        s = Skill.objects.create(skill=i, user_profile=random.choice(users))
        s.save()

    # Random date generation
    year = random.choice(range(2015, 2018))
    month = random.choice(range(1, 13))
    day = random.choice(range(1, 29))
    date = datetime(year, month, day)

    # Hackathon model
    hacks = ['MSF', 'FLOCHAT', 'SIH', 'MONEY CONTROL', 'HACK IN NORTH']
    for i in hacks:
        s = Hackathon.objects.create(CompetitionName=i, 
            student_profile=random.choice(users), Date=date)
        s.save()

    # Education model
    for i in 'qwertyuiolkjhgfdsazxcvbnm':
        i = Education.objects.create(student_profile=random.choice(users),
            sem1_gpa=round(np.random.uniform(6, 10), 2),
            sem2_gpa= round(np.random.uniform(6, 10), 2),
            sem3_gpa=round(np.random.uniform(6, 10), 2),
            sem4_gpa=round(np.random.uniform(6, 10), 2),
            sem5_gpa=round(np.random.uniform(6, 10), 2),
            sem6_gpa=round(np.random.uniform(6, 10), 2),
            sem7_gpa=round(np.random.uniform(6, 10), 2),
            sem8_gpa=round(np.random.uniform(6, 10), 2))
        i.save()

    # Project model:
    skills = Skill.objects.all()
    skills = [s for s in skills]
    for i in 'qwertyuiolkjhgfdsazxcvbnm':
        i = Project.objects.create(student_profile=random.choice(users), 
            projectUnderTeacher=random.choice(teachers), skill=random.choice(skills), ProjName=i)
        i.save()

    # Committee
    for i in 'qwertyuiolkjhgfdsazxcvbnm':
        i = Committee.objects.create(employee=random.choice(users), OrganisationName='ACM', 
            YourPosition='Tech Head')
        i.save()

    # KT model
    edu = Education.objects.all()
    edu = [s for s in edu]
    subj = ['tcs', 'dbms', 'ds', 'oopm', 'maths-1', 'physics', 'chemistry']

    for i in range(0,48):
        u = KT.objects.create(education=random.choice(edu), subject_name=random.choice(subj))
        if i % 8 == 0:
            u.subject_semester = "Semester 1"
        elif i % 8 == 1:
            u.subject_semester = "Semester 2"
        elif i % 8 == 2:
            u.subject_semester = "Semester 3"
        elif i % 8 == 3:
            u.subject_semester = "Semester 4"
        elif i % 8 == 4:
            u.subject_semester = "Semester 5"
        elif i % 8 == 5:
            u.subject_semester = "Semester 6"
        elif i % 8 == 6:
            u.subject_semester = "Semester 7"
        elif i % 8 == 7:
            u.subject_semester = "Semester 8"
        u.save()

    # Research Paper
    for i in 'qwertyuiolkjhgfdsazxcvbnm':
        i = ResearchPaper.objects.create(student=random.choice(users), 
            Title='Dropout: NN', Publication='IEEE', Published_under=random.choice(teachers))
        i.save()

# TO RUN THIS SCRIPT -
#
# python manage.py shell
#
# from user_profile.dummy import *
#
# fill()
# please follow the above order and make sure you dont have your own users
# registered pehle se or it'll just clash
# just have a superuser and then run the above commands
