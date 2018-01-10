from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy
# from django.views import generic
from django.contrib.auth import authenticate
# from django.views.generic import View
from .models import StudentProfile
from django.http import HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile/profile.html', {})
    else:
        if request.method == 'POST':
            username = request.POST.get('Sap_Id', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            Sap_Id = request.POST.get('Sap_Id', '')

            if StudentProfile.objects.filter(username=username).exists():
                error = 'The Sap_id is already in use by another account.'
                return render(request, 'user_profile/registration_form.html', {'error': error})

            else:
                user = StudentProfile.objects.create(username=username, email=email, Sap_Id=Sap_Id)
                user.is_superuser = False
                user.is_staff = False
                user.set_password(password)
                user.save()
        else:
            return render(request, 'user_profile/registration_form.html', {})


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
                    return HttpResponse("Your Rango account is disabled.")
            else:
                error = 'The Sap_id or the password is incorrect.'
                return render(request, 'user_profile/login.html', {'error': error})
        else:
            return render(request, 'user_profile/login.html', {})


def logout(request):
    auth_logout(request)
    return render(request, 'user_profile/login.html', {})
