from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import (StudentProfile, TeacherProfile, Internship, Project, Committee, ResearchPaper, BeProject,
                     Hackathon, Skill)
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.shortcuts import get_object_or_404

import datetime


def register(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile/profile.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('Sap_Id', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            Sap_Id = request.POST.get('Sap_Id', '')

            if User.objects.filter(username=username).exists():
                error = 'The Sap_id is already in use by another account.'
                return render(request, 'user_profile/registration.html', {'error': error})

            else:
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                content_type = ContentType.objects.get_for_model(StudentProfile)
                permission = Permission.objects.get(content_type=content_type, codename='view_student')
                user.user_permissions.add(permission)
                student = StudentProfile.objects.create(student=user, Sap_Id=Sap_Id)
                student.save()
                return render(request, 'user_profile/profile.html', {})
        else:
            return render(request, 'user_profile/registration.html', {})


def user_login(request):
    if request.user.is_authenticated:
            return render(request, 'user_profile/profile.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'user_profile/profile.html', {})
                else:
                    error = 'Your account is disabled.'
                    return render(request, 'user_profile/login.html', {'error': error})
            else:
                error = 'Incorrect Username or Password'
                return render(request, 'user_profile/login.html', {'error': error})
        else:
            return render(request, 'user_profile/login.html', {})


def register_teacher(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile/teacherprofile.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('Sap_Id', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            Sap_Id = request.POST.get('Sap_Id', '')

            if User.objects.filter(username=username).exists():
                error = 'The Sap_id is already in use by another account.'
                return render(request, 'user_profile/registration_teacher.html', {'error': error})

            else:
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                content_type = ContentType.objects.get_for_model(TeacherProfile)
                permission = Permission.objects.get(content_type=content_type, codename='view_teacher')
                user.user_permissions.add(permission)
                content_type = ContentType.objects.get_for_model(StudentProfile)
                permission = Permission.objects.get(content_type=content_type, codename='view_student')
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(StudentProfile)
                permission = Permission.objects.get(codename='delete_studentprofile', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(Internship)
                permission = Permission.objects.get(codename='delete_internship', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(Project)
                permission = Permission.objects.get(codename='delete_project', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(Committee)
                permission = Permission.objects.get(codename='delete_committee', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(ResearchPaper)
                permission = Permission.objects.get(codename='delete_researchpaper', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(BeProject)
                permission = Permission.objects.get(codename='delete_beproject', content_type=ct)
                user.user_permissions.add(permission)
                user.save()
                teacher = TeacherProfile.objects.create(teacher=user, Sap_Id=Sap_Id)
                teacher.save()
                return render(request, 'user_profile/teacherprofile.html', {})
        else:
            return render(request, 'user_profile/registration_teacher.html', {})


def user_login_teacher(request):
    if request.user.is_authenticated:
            return render(request, 'user_profile/teacherprofile.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'user_profile/teacherprofile.html', {})
                else:
                    error = 'Your account is disabled.'
                    return render(request, 'user_profile/teacher_login.html', {'error': error})
            else:
                error = 'Incorrect Username or Password'
                return render(request, 'user_profile/teacher_login.html', {'error': error})
        else:
            return render(request, 'user_profile/teacher_login.html', {})


def logout_student(request):
    auth_logout(request)
    return redirect(reverse('login'))


def logout_teacher(request):
    auth_logout(request)
    return redirect(reverse('user_login_teacher'))


def logout_recruiter(request):
    auth_logout(request)
    return redirect(reverse('user_login_recruiter'))


def user_login_recruiter(request):
    if request.user.is_authenticated:
            return render(request, 'user_profile/recruiter.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return render(request, 'user_profile/recruiter.html', {})
                else:
                    error = 'Your account is disabled.'
                    return render(request, 'user_profile/login_recruiter.html', {'error': error})
            else:
                error = 'Incorrect Username or Password'
                return render(request, 'user_profile/login_recruiter.html', {'error': error})
        else:
            return render(request, 'user_profile/login_recruiter.html', {})


def student_profile(request, sapid):
    if request.user.is_authenticated:
        student = get_object_or_404(StudentProfile, Sap_Id=sapid)
        return render(request, 'user_profile/student_profile.html', {'student': student})
    else:
        return HttpResponse("Please Login")


def student_editprofile(request, sapid):
    if request.user.is_authenticated:
        student = get_object_or_404(StudentProfile, Sap_Id=sapid)

        if request.method == 'POST':
            bio = request.POST.get('bio', '')
            skill = request.POST.get('skill', '')
            mobileNo = request.POST.get('mobileNo', '')
            CompetitionName = request.POST.get('CompetitionName', '')
            company = request.POST.get('company', '')
            ProjName = request.POST.get('ProjName', '')
            OrganisationName = request.POST.get('OrganisationName', '')
            Title = request.POST.get('Title', '')
            BeProjName = request.POST.get('BeProjName', '')
            student.bio = bio
            student.mobileNo = mobileNo
            if CompetitionName != '':
                Date = request.POST.get('Date')
                Desc = request.POST.get('Desc', '')
                URL = request.POST.get('URL', '')
                image1 = request.FILES.get('hackathonimage1')
                hackathon = Hackathon(CompetitionName=CompetitionName, Desc=Desc, URL=URL, image1=image1)
                if Date != '':
                    hackathon.Date = datetime.datetime.strptime(Date, '%Y-%m-%d').date()
                hackathon.save()
                student.hackathon.add(hackathon)
            if skill != '':
                skills = Skill(skill=skill)
                skills.save()
                student.skills.add(skills)
            if company != '':
                Position = request.POST.get('Position', '')
                Loc = request.POST.get('Loc', '')
                desc = request.POST.get('desc', '')
                From = request.POST.get('From')
                To = request.POST.get('To')
                image1 = request.FILES.get('internshipimage1')
                internship = Internship(company=company, Position=Position, Loc=Loc, desc=desc,
                                        employee=student, image1=image1)
                if From != '' and To != '':
                    internship.From = datetime.datetime.strptime(From, '%Y-%m-%d').date()
                    internship.To = datetime.datetime.strptime(To, '%Y-%m-%d').date()
                internship.save()
            if ProjName != '':
                ProjURL = request.POST.get('ProjURL', '')
                ProjDesc = request.POST.get('ProjDesc', '')
                projectUnderTeacher = request.POST.get('projectUnderTeacher', '')
                image1 = request.FILES.get('projectimage1')
                project = Project(student=student, ProjName=ProjName, ProjURL=ProjURL, ProjDesc=ProjDesc, image1=image1)
                if projectUnderTeacher != '':
                    projectUnderTeacher = get_object_or_404(TeacherProfile, Sap_Id=projectUnderTeacher)
                    project.projectUnderTeacher = projectUnderTeacher
                project.save()
            if OrganisationName != '':
                YourPosition = request.POST.get('YourPosition', '')
                Loc = request.POST.get('committeeLoc', '')
                dateFrom = request.POST.get('dateFrom')
                dateTo = request.POST.get('dateTo')
                Desc = request.POST.get('committeeDesc', '')
                image1 = request.FILES.get('committeeimage1')
                committee = Committee(employee=student, OrganisationName=OrganisationName, YourPosition=YourPosition,
                                      Loc=Loc, Desc=Desc, image1=image1)
                if dateFrom != '' and dateTo != '':
                    internship.From = datetime.datetime.strptime(dateFrom, '%Y-%m-%d').date()
                    internship.To = datetime.datetime.strptime(dateTo, '%Y-%m-%d').date()
                committee.save()
            if Title != '':
                Publication = request.POST.get('Publication', '')
                DateOfPublication = request.POST.get('DateOfPublication')
                Desc = request.POST.get('researchdesc', '')
                LinkToPaper = request.POST.get('LinkToPaper', '')
                PaperId = request.POST.get('PaperId', '')
                Published_under = request.POST.get('Published_under', '')
                image1 = request.FILES.get('researchimage1')
                researchpaper = ResearchPaper(student=student, Title=Title, Desc=Desc, LinkToPaper=LinkToPaper,
                                              Publication=Publication, PaperId=PaperId, image1=image1)
                if Published_under != '':
                    Published_under = get_object_or_404(TeacherProfile, Sap_Id=Published_under)
                    researchpaper.Published_under = Published_under
                if DateOfPublication != '':
                    researchpaper.DateOfPublication = datetime.datetime.strptime(DateOfPublication, '%Y-%m-%d').date()
                researchpaper.save()
            if BeProjName != '':
                ProjURL = request.POST.get('BeProjURL', '')
                ProjDesc = request.POST.get('BeProjDesc', '')
                projectUnderTeacher = request.POST.get('BeprojectUnderTeacher', '')
                image1 = request.FILES.get('Beprojectimage1')
                teammate1 = request.POST.get('teammate1')
                teammate2 = request.POST.get('teammate2')
                teammate3 = request.POST.get('teammate3')
                teammate4 = request.POST.get('teammate4')
                beproject = BeProject(student=student, ProjName=ProjName, ProjURL=ProjURL, ProjDesc=ProjDesc,
                                      image1=image1)
                if teammate1:
                    teammate1 = get_object_or_404(StudentProfile, Sap_Id=teammate1)
                    teammate1.beteammate.clear()
                    beproject.save()
                    beproject.teammates.add(teammate1)
                if teammate2:
                    teammate2 = get_object_or_404(StudentProfile, Sap_Id=teammate2)
                    teammate2.beteammate.clear()
                    beproject.teammates.add(teammate2)
                if teammate3:
                    teammate3 = get_object_or_404(StudentProfile, Sap_Id=teammate3)
                    teammate3.beteammate.clear()
                    beproject.teammates.add(teammate3)
                if teammate4:
                    teammate4 = get_object_or_404(StudentProfile, Sap_Id=teammate4)
                    teammate4.beteammate.clear()
                    beproject.teammates.add(teammate4)
                if projectUnderTeacher != '':
                    projectUnderTeacher = get_object_or_404(TeacherProfile, Sap_Id=projectUnderTeacher)
                    beproject.projectUnderTeacher = projectUnderTeacher
                beproject.save()
            student.save()
            return render(request, 'user_profile/student_profile.html', {'student': student})
        else:
            beproject = student.beprojects.all()[0]
            context = {'student': student,
                       'ProjName': beproject.ProjName,
                       'ProjURL': beproject.ProjURL,
                       'ProjDesc': beproject.ProjDesc,
                       'Teacher': beproject.projectUnderTeacher.Sap_Id}
            for i, teammate in enumerate(beproject.teammates.all()):
                context['teammate' + str(i + 1)] = teammate.Sap_Id
            return render(request, 'user_profile/edit_student_profile.html', context)
    else:
        return HttpResponse("Please Login")
