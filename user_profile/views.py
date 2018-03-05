from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import (StudentProfile, TeacherProfile, Internship, Project, Committee, ResearchPaper, BeProject,
                     Hackathon, Skill, Education)
from .models import (HistoricalInternship, HistoricalProject, HistoricalCommittee, HistoricalResearchPaper,
                     HistoricalBeProject)
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
import collections
from django.utils.dateformat import format
import datetime


def show_rollingform(request):
    return render(request, 'user_profile/edit_student_profile.html')


def register(request):
    if request.user.is_authenticated:
        student_profile = StudentProfile.objects.get(student=request.user)
        student_profile_url = '/student_profile/' + str(student_profile.id)
        return HttpResponseRedirect(student_profile_url)
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
                content_type = ContentType.objects.get_for_model(
                    StudentProfile)
                permission = Permission.objects.get(
                    content_type=content_type, codename='view_student')
                user.user_permissions.add(permission)
                student = StudentProfile.objects.create(
                    student=user, Sap_Id=Sap_Id)
                student.save()
                student_profile_url = '/student_profile/' + str(student.id)
                return HttpResponseRedirect(student_profile_url)
                # return render(request, 'user_profile/profile.html', {"student": student})
        else:
            return render(request, 'user_profile/registration.html', {})


def user_login(request):
    if request.user.is_authenticated:
        student_profile = StudentProfile.objects.get(student=request.user)
        student_profile_url = '/student_profile/' + str(student_profile.id)
        return HttpResponseRedirect(student_profile_url)
    else:
        if request.method == 'POST':
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    # return render(request, 'user_profile/profile.html', {})
                    student_profile = StudentProfile.objects.get(
                        student=request.user)
                    student_profile_url = '/student_profile/' + \
                        str(student_profile.id)
                    return HttpResponseRedirect(student_profile_url)
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
                content_type = ContentType.objects.get_for_model(
                    TeacherProfile)
                permission = Permission.objects.get(
                    content_type=content_type, codename='view_teacher')
                user.user_permissions.add(permission)
                content_type = ContentType.objects.get_for_model(
                    StudentProfile)
                permission = Permission.objects.get(
                    content_type=content_type, codename='view_student')
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(StudentProfile)
                permission = Permission.objects.get(
                    codename='delete_studentprofile', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(Internship)
                permission = Permission.objects.get(
                    codename='delete_internship', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(Project)
                permission = Permission.objects.get(
                    codename='delete_project', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(Committee)
                permission = Permission.objects.get(
                    codename='delete_committee', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(ResearchPaper)
                permission = Permission.objects.get(
                    codename='delete_researchpaper', content_type=ct)
                user.user_permissions.add(permission)
                ct = ContentType.objects.get_for_model(BeProject)
                permission = Permission.objects.get(
                    codename='delete_beproject', content_type=ct)
                user.user_permissions.add(permission)
                user.save()
                teacher = TeacherProfile.objects.create(
                    teacher=user, Sap_Id=Sap_Id)
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
    return redirect(reverse('user_profile:user_login'))


def logout_teacher(request):
    auth_logout(request)
    return redirect(reverse('user_profile:user_login_teacher'))


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


def student_profile(request, id):
    if request.user.is_authenticated:
        # student = get_object_or_404(StudentProfile, Sap_Id=sapid)
        # line chart of marks
        # gpa_list = [gpa for gpa in student.education.all()[0].__dict__.values()]

        student = StudentProfile.objects.get(id=id)
        try:
            education = Education.objects.get(student_profile=student)
            sem1gpa = education.sem1_gpa
            sem2gpa = education.sem2_gpa
            sem3gpa = education.sem3_gpa
            sem4gpa = education.sem4_gpa
            sem5gpa = education.sem5_gpa
            sem6gpa = education.sem6_gpa
            sem7gpa = education.sem7_gpa
            sem8gpa = education.sem8_gpa
            gpa_list = [sem1gpa, sem2gpa, sem3gpa, sem4gpa,
                        sem5gpa, sem6gpa, sem7gpa, sem8gpa]
        except Education.DoesNotExist:
            gpa_list = []

        if Project.objects.filter(student_profile=student).exists():
            project_objects = Project.objects.filter(student_profile=student)
            projectskill_stats = [
                project.skill.skill for project in project_objects]
            projectskill_stats = dict(collections.Counter(projectskill_stats))
            print(projectskill_stats)
        else:
            projectskill_stats = {}
        return render(request, 'user_profile/profile.html',
                      {'gpa_list': gpa_list, 'projectskill_stats': projectskill_stats})
    else:
        return HttpResponse("Please Login")


def student_editprofile(request, sapid):
    if request.user.is_authenticated:
        student = get_object_or_404(StudentProfile, Sap_Id=sapid)

        if request.method == 'POST':
            bio = request.POST.get('bio', '')
            skill = request.POST.get('skill', '')
            mobileNo = request.POST.get('mobileNo', '')
            photo = request.FILES.get('photo', '')
            year = request.POST.get('year', '')
            CompetitionName = request.POST.get('CompetitionName', '')
            company = request.POST.get('company', '')
            ProjName = request.POST.get('ProjName', '')
            OrganisationName = request.POST.get('OrganisationName', '')
            Title = request.POST.get('Title', '')
            BeProjName = request.POST.get('BeProjName', '')
            student.bio = bio
            student.mobileNo = mobileNo
            student.year = year
            student.photo = photo
            if CompetitionName != '':
                Date = request.POST.get('Date')
                Desc = request.POST.get('Desc', '')
                URL = request.POST.get('URL', '')
                image1 = request.FILES.get('hackathonimage1')
                hackathon = Hackathon(
                    CompetitionName=CompetitionName, Desc=Desc, URL=URL, image1=image1)
                if Date != '':
                    hackathon.Date = datetime.datetime.strptime(
                        Date, '%Y-%m-%d').date()
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
                    internship.From = datetime.datetime.strptime(
                        From, '%Y-%m-%d').date()
                    internship.To = datetime.datetime.strptime(
                        To, '%Y-%m-%d').date()
                internship.save()
            if ProjName != '':
                ProjURL = request.POST.get('ProjURL', '')
                ProjDesc = request.POST.get('ProjDesc', '')
                projectUnderTeacher = request.POST.get(
                    'projectUnderTeacher', '')
                image1 = request.FILES.get('projectimage1')
                project = Project(student=student, ProjName=ProjName,
                                  ProjURL=ProjURL, ProjDesc=ProjDesc, image1=image1)
                if projectUnderTeacher != '':
                    projectUnderTeacher = get_object_or_404(
                        TeacherProfile, Sap_Id=projectUnderTeacher)
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
                    internship.From = datetime.datetime.strptime(
                        dateFrom, '%Y-%m-%d').date()
                    internship.To = datetime.datetime.strptime(
                        dateTo, '%Y-%m-%d').date()
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
                    Published_under = get_object_or_404(
                        TeacherProfile, Sap_Id=Published_under)
                    researchpaper.Published_under = Published_under
                if DateOfPublication != '':
                    researchpaper.DateOfPublication = datetime.datetime.strptime(
                        DateOfPublication, '%Y-%m-%d').date()
                researchpaper.save()
            if BeProjName != '':
                ProjURL = request.POST.get('BeProjURL', '')
                ProjDesc = request.POST.get('BeProjDesc', '')
                projectUnderTeacher = request.POST.get(
                    'BeprojectUnderTeacher', '')
                image1 = request.FILES.get('Beprojectimage1')
                teammate1 = request.POST.get('teammate1')
                teammate2 = request.POST.get('teammate2')
                teammate3 = request.POST.get('teammate3')
                teammate4 = request.POST.get('teammate4')
                try:
                    beproject = BeProject.objects.get(student=student)
                except BeProject.DoesNotExist:
                    beproject = BeProject(student=student)
                finally:
                    beproject.ProjName = BeProjName
                    beproject.ProjURL = ProjURL
                    beproject.ProjDesc = ProjDesc
                    beproject.image1 = image1
                    beproject.teammates.clear()
                    if teammate1:
                        teammate1 = get_object_or_404(
                            StudentProfile, Sap_Id=teammate1)
                        teammate1.beteammate.clear()
                        beproject.teammates.add(teammate1)
                    if teammate2:
                        teammate2 = get_object_or_404(
                            StudentProfile, Sap_Id=teammate2)
                        teammate2.beteammate.clear()
                        beproject.teammates.add(teammate2)
                    if teammate3:
                        teammate3 = get_object_or_404(
                            StudentProfile, Sap_Id=teammate3)
                        teammate3.beteammate.clear()
                        beproject.teammates.add(teammate3)
                    if teammate4:
                        teammate4 = get_object_or_404(
                            StudentProfile, Sap_Id=teammate4)
                        teammate4.beteammate.clear()
                        beproject.teammates.add(teammate4)
                    if projectUnderTeacher != '':
                        projectUnderTeacher = get_object_or_404(
                            TeacherProfile, Sap_Id=projectUnderTeacher)
                        beproject.projectUnderTeacher = projectUnderTeacher
                        beproject.save()
            student.save()
            return render(request, 'user_profile/student_profile.html', {'student': student})
        else:
            beproject = student.beprojects.all()
            context = {}
            if beproject:
                context = {'ProjName': beproject[0].ProjName,
                           'ProjURL': beproject[0].ProjURL,
                           'ProjDesc': beproject[0].ProjDesc,
                           }
                teacher = beproject[0].projectUnderTeacher
                if teacher:
                    context['Teacher'] = teacher.Sap_Id
                for i, teammate in enumerate(beproject[0].teammates.all()):
                    context['teammate' + str(i + 1)] = teammate.Sap_Id
            context['student'] = student
            return render(request, 'user_profile/edit_student_profile.html', context)
    else:
        return HttpResponse("Please Login")


def searchany(request):
    context = {}
    if request.method == 'POST':
        searchquery = request.POST.get('searchany')
        # queryset=StudentProfile.objects.filter(department__trigram_similar=searchquery)
        dept_vector = SearchVector('department', 'bio', 'mobileNo')
        skill_vector = SearchVector('skill')
        hackathon_vector = SearchVector('CompetitionName', 'Desc', 'URL')
        internship_vector = SearchVector('company')
        project_vector = SearchVector('ProjName')
        beproject_vector = SearchVector('ProjName')

        # bio_vector = SearchVector('bio')
        queryset = StudentProfile.objects.annotate(
            search=dept_vector).filter(search=searchquery)
        skillset = Skill.objects.annotate(
            search=skill_vector).filter(search=searchquery)
        hackathonset = Hackathon.objects.annotate(
            search=hackathon_vector).filter(search=searchquery)
        internshipset = Internship.objects.annotate(
            search=internship_vector).filter(search=searchquery)
        projectset = Project.objects.annotate(
            search=project_vector).filter(search=searchquery)
        beprojectset = BeProject.objects.annotate(
            search=beproject_vector).filter(search=searchquery)

        # StudentProfile.objects.annotate(search=skill_vector).filter(search=searchquery)
        context['queryset'] = queryset
        context['skillset'] = skillset
        context['hackathonset'] = hackathonset
        context['internshipset'] = internshipset
        context['projectset'] = projectset
        context['beprojectset'] = beprojectset

        return render(request, 'user_profile/searchany.html', context)
    else:
        return render(request, 'user_profile/searchany.html')


def notifs(request):
    # Dictionary for storing internship changes with key as Sap_Id
    listed = {}
    for student in StudentProfile.objects.all():
        listed[student.Sap_Id] = []
        for internship in student.internships.all():
            a = []
            a.append(internship)
            cmp1 = []
            cmp2 = []
            count = 0
            c1 = internship.history.all().count()
            if c1 == 1:
                break
            for x in internship.history.all():
                b = x.history_date
                k = HistoricalInternship.objects.get(history_date=b)
                if count == 0:
                    a.append(b)
                    cmp1.append(k.company)
                    cmp1.append(k.Position)
                    cmp1.append(k.Loc)
                    cmp1.append(k.From)
                    cmp1.append(k.To)
                    cmp1.append(k.desc)
                    cmp1.append(k.Certificate)
                    cmp1.append(k.image1)
                if count == 1:
                    cmp2.append(k.company)
                    cmp2.append(k.Position)
                    cmp2.append(k.Loc)
                    cmp2.append(k.From)
                    cmp2.append(k.To)
                    cmp2.append(k.desc)
                    cmp2.append(k.Certificate)
                    cmp2.append(k.image1)
                if count == 2:
                    break
                count = count + 1
            if cmp1[0] != cmp2[0]:
                a.append('company')
            if cmp1[1] != cmp2[1]:
                a.append('Position')
            if cmp1[2] != cmp2[2]:
                a.append('Loc')
            if cmp1[3] != cmp2[3]:
                a.append('Date Joined')
            if cmp1[4] != cmp2[4]:
                a.append('Date To')
            if cmp1[5] != cmp2[5]:
                a.append('Description')
            if cmp1[6] != cmp2[6]:
                a.append('Certificate')
            if cmp1[7] != cmp2[7]:
                a.append('Screenshot')
            if len(a) != 2:
                listed[student.Sap_Id].append(a)

    # Dictionary for storing projects changes with key as Sap_Id
    projects = {}
    for student in StudentProfile.objects.all():
        projects[student.Sap_Id] = []
        for project in student.projects.all():
            a = []
            a.append(project)
            cmp1 = []
            cmp2 = []
            count = 0
            c1 = project.history.all().count()
            if c1 == 1:
                break
            for x in project.history.all():
                b = x.history_date
                k = HistoricalProject.objects.get(history_date=b)
                if count == 0:
                    a.append(b)
                    cmp1.append(k.ProjName)
                    cmp1.append(k.ProjURL)
                    cmp1.append(k.ProjDesc)
                    cmp1.append(k.image1)
                if count == 1:
                    cmp2.append(k.ProjName)
                    cmp2.append(k.ProjURL)
                    cmp2.append(k.ProjDesc)
                    cmp2.append(k.image1)
                if count == 2:
                    break
                count = count + 1
            if cmp1[0] != cmp2[0]:
                a.append('Project Name')
            if cmp1[1] != cmp2[1]:
                a.append('Project URL')
            if cmp1[2] != cmp2[2]:
                a.append('Project Description')
            if cmp1[3] != cmp2[3]:
                a.append('Screenshot')
            if len(a) != 2:
                projects[student.Sap_Id].append(a)

        # Dictionary for storing beprojects changes with key as Sap_Id
        beprojects = {}
        for student in StudentProfile.objects.all():
            beprojects[student.Sap_Id] = []
            for beproject in student.beprojects.all():
                a = []
                a.append(beproject)
                cmp1 = []
                cmp2 = []
                count = 0
                c1 = beproject.history.all().count()
                if c1 == 1:
                    break
                for x in beproject.history.all():
                    b = x.history_date
                    k = HistoricalBeProject.objects.get(history_date=b)
                    if count == 0:
                        a.append(b)
                        cmp1.append(k.ProjName)
                        cmp1.append(k.ProjURL)
                        cmp1.append(k.ProjDesc)
                        cmp1.append(k.image1)
                    if count == 1:
                        cmp2.append(k.ProjName)
                        cmp2.append(k.ProjURL)
                        cmp2.append(k.ProjDesc)
                        cmp2.append(k.image1)
                    if count == 2:
                        break
                    count = count + 1
                if cmp1[0] != cmp2[0]:
                    a.append('Project Name')
                if cmp1[1] != cmp2[1]:
                    a.append('Project URL')
                if cmp1[2] != cmp2[2]:
                    a.append('Project Description')
                if cmp1[3] != cmp2[3]:
                    a.append('Screenshot')
                if len(a) != 2:
                    beprojects[student.Sap_Id].append(a)

        # Dictionary for storing committee changes with key as Sap_Id
        committee = {}
        for student in StudentProfile.objects.all():
            committee[student.Sap_Id] = []
            for committe in student.committee.all():
                a = []
                a.append(committe)
                cmp1 = []
                cmp2 = []
                count = 0
                c1 = committe.history.all().count()
                if c1 == 1:
                    break
                for x in committe.history.all():
                    b = x.history_date
                    k = HistoricalCommittee.objects.get(history_date=b)
                    if count == 0:
                        a.append(b)
                        cmp1.append(k.OrganisationName)
                        cmp1.append(k.YourPosition)
                        cmp1.append(k.Loc)
                        cmp1.append(k.dateFrom)
                        cmp1.append(k.dateTo)
                        cmp1.append(k.Desc)
                        cmp1.append(k.Certificate)
                        cmp1.append(k.image1)
                    if count == 1:
                        cmp2.append(k.OrganisationName)
                        cmp2.append(k.YourPosition)
                        cmp2.append(k.Loc)
                        cmp2.append(k.dateFrom)
                        cmp2.append(k.dateTo)
                        cmp2.append(k.Desc)
                        cmp2.append(k.Certificate)
                        cmp2.append(k.image1)
                    if count == 2:
                        break
                    count = count + 1
                if cmp1[0] != cmp2[0]:
                    a.append('Company')
                if cmp1[1] != cmp2[1]:
                    a.append('Position')
                if cmp1[2] != cmp2[2]:
                    a.append('Location')
                if cmp1[3] != cmp2[3]:
                    a.append('Date Joined')
                if cmp1[4] != cmp2[4]:
                    a.append('Date To')
                if cmp1[5] != cmp2[5]:
                    a.append('Description')
                if cmp1[6] != cmp2[6]:
                    a.append('Certificate')
                if cmp1[7] != cmp2[7]:
                    a.append('Screenshot')
                if len(a) != 2:
                    committee[student.Sap_Id].append(a)

        # Dictionary for storing ResearchPaper changes with key as Sap_Id
        researchpaper = {}
        for student in StudentProfile.objects.all():
            researchpaper[student.Sap_Id] = []
            for research in student.researchpaper.all():
                a = []
                a.append(research)
                cmp1 = []
                cmp2 = []
                count = 0
                c1 = research.history.all().count()
                if c1 == 1:
                    break
                for x in research.history.all():
                    b = x.history_date
                    k = HistoricalResearchPaper.objects.get(history_date=b)
                    if count == 0:
                        a.append(b)
                        cmp1.append(k.Title)
                        cmp1.append(k.Publication)
                        cmp1.append(k.DateOfPublication)
                        cmp1.append(k.Desc)
                        cmp1.append(k.LinkToPaper)
                        cmp1.append(k.Desc)
                        cmp1.append(k.PaperId)
                        cmp1.append(k.image1)
                    if count == 1:
                        cmp2.append(k.Title)
                        cmp2.append(k.Publication)
                        cmp2.append(k.DateOfPublication)
                        cmp2.append(k.Desc)
                        cmp2.append(k.LinkToPaper)
                        cmp2.append(k.Desc)
                        cmp2.append(k.PaperId)
                        cmp2.append(k.image1)
                    if count == 2:
                        break
                    count = count + 1
                if cmp1[0] != cmp2[0]:
                    a.append('Title')
                if cmp1[1] != cmp2[1]:
                    a.append('Publication')
                if cmp1[2] != cmp2[2]:
                    a.append('DateOfPublication')
                if cmp1[3] != cmp2[3]:
                    a.append('Description')
                if cmp1[4] != cmp2[4]:
                    a.append('LinkToPaper')
                if cmp1[5] != cmp2[5]:
                    a.append('Description')
                if cmp1[6] != cmp2[6]:
                    a.append('PaperId')
                if cmp1[7] != cmp2[7]:
                    a.append('Screenshot')
                if len(a) != 2:
                    researchpaper[student.Sap_Id].append(a)

    return render(request, 'user_profile/notifs.html', {'listed': listed, 'projects': projects,
                                                        'beprojects': beprojects,
                                                        'committee': committee,
                                                        'researchpaper': researchpaper})


def student_list(request):
    if request.method == 'POST':
        most_common_to_take = 3
        skills = Skill.objects.all()
        list_of_skills = [skill.skill for skill in skills]
        most_frequent = collections.Counter(
            list_of_skills).most_common(most_common_to_take)
        skillss = [skill[0] for skill in most_frequent]

        year = request.POST.getlist('year[]')
        skills = request.POST.getlist('skills[]')
        print(year)
        print(skills)

        if year and skills:
            result = StudentProfile.objects.filter(year__in=year).filter(
                skills__skill__in=skills).distinct()
            projects = Project.objects.filter(
                skill__skill__in=skills).distinct()
        elif year:
            result = StudentProfile.objects.filter(year__in=year)
            projects = []
        elif skills:
            result = StudentProfile.objects.filter(
                skills__skill__in=skills).distinct()
            projects = Project.objects.filter(
                skill__skill__in=skills).distinct()
        else:
            result = []
            projects = []
        print(result, "res")

        return render(request, 'user_profile/search.html', {'result': result, 'skills': skillss, 'projects': projects})
    else:
        most_common_to_take = 3
        skills = Skill.objects.all()
        list_of_skills = [skill.skill for skill in skills]
        most_frequent = collections.Counter(
            list_of_skills).most_common(most_common_to_take)
        skillss = [skill[0] for skill in most_frequent]
        return render(request, 'user_profile/search.html', {'skills': skillss})


def teacher_dashboard(request):
    # calculating most common skills
    most_common_to_take = 3
    skills = Skill.objects.all()
    list_of_skills = [skill.skill for skill in skills]
    most_frequent_skills = collections.Counter(
        list_of_skills).most_common(most_common_to_take)
    print(most_frequent_skills)
    # calculating year-wise internship stats
    internship_objects = Internship.objects.all()
    intern_stats = [
        internship.employee.year for internship in internship_objects]
    intern_stats = collections.Counter(intern_stats)
    print(intern_stats)

    # list of all pointers
    sem1_list = [education.sem1_gpa for education in Education.objects.all(
    ) if education.sem1_gpa is not None]
    # sem1_list = filter(None, sem1_list)
    sem2_list = [education.sem2_gpa for education in Education.objects.all(
    ) if education.sem2_gpa is not None]
    sem3_list = [education.sem3_gpa for education in Education.objects.all(
    ) if education.sem3_gpa is not None]
    sem4_list = [education.sem4_gpa for education in Education.objects.all(
    ) if education.sem4_gpa is not None]
    sem5_list = [education.sem5_gpa for education in Education.objects.all(
    ) if education.sem5_gpa is not None]
    sem6_list = [education.sem6_gpa for education in Education.objects.all(
    ) if education.sem6_gpa is not None]
    sem7_list = [education.sem7_gpa for education in Education.objects.all(
    ) if education.sem7_gpa is not None]
    sem8_list = [education.sem8_gpa for education in Education.objects.all(
    ) if education.sem8_gpa is not None]
    print(sem1_list, sem2_list, sem3_list, sem4_list,
          sem5_list, sem6_list, sem7_list, sem8_list)

    # internship time stamps
    intern_dates = [format(internship.From, 'U')
                    for internship in Internship.objects.all()]
    intern_dates.sort()
    intern_date = [int(x) - int(intern_dates[0]) for x in intern_dates]
    print(intern_dates)
    print(intern_date)
    return HttpResponse(intern_stats)


def education_graphs():
    pass


def view_internship(request, internshipid):
    internship = Internship.objects.get(id=internshipid)
    # return render(request, '',{'internship':internship})
    return HttpResponse(internship.company)


def view_hackathon(request, hackathonid):
    hackathon = Hackathon.objects.get(id=hackathonid)
    # return render(request, '',{'hackathon':hackathon})
    return HttpResponse(hackathon.CompetitionName)


def view_project(request, projectid):
    project = Project.objects.get(id=projectid)
    # return render(request, '',{'project':project})
    return HttpResponse(project.ProjName)


def view_beproject(request, beprojectid):
    beproject = BeProject.objects.get(id=beprojectid)
    # return render(request, '',{'beproject':beproject})
    return HttpResponse(beproject.ProjName)


def show_edit_studentprofile(request):
    if request.user.is_authenticated:
        student_profile = StudentProfile.objects.get(student=request.user)
        return render(request, 'user_profile/edit_student_profile_2.html', {'student_profile': student_profile})
    else:
        return HttpResponseRedirect('/login/student/')


def edit_basic_info(request, id):
    if request.method == 'POST':
        student_profile = StudentProfile.objects.get(id=id)
        student_profile.first_name = request.POST.get('fname')
        student_profile.last_name = request.POST.get('lname')
        student_profile.department = request.POST.get('department')
        print(request.POST.get('gender'))
        student_profile.gender = request.POST.get('gender')
        student_profile.mobileNo = request.POST.get('mobileNo')
        student_profile.save()
        print('IT WORKS ASSHOLE')
        return HttpResponse('done')