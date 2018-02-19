from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/student/$', views.register, name='register'),
    url(r'^login/student/$', views.user_login, name='login'),
    url(r'^register/teacher/$', views.register_teacher, name='register_teacher'),
    url(r'^login/teacher/$', views.user_login_teacher, name='user_login_teacher'),
    url(r'^logout/student/$', views.logout_student, name='logout_student'),
    url(r'^logout/teacher/$', views.logout_teacher, name='logout_teacher'),
    url(r'^login/recruiter/$', views.user_login_recruiter,
        name='user_login_recruiter'),
    url(r'^logout/recruiter/$', views.logout_recruiter, name='logout_recruiter'),
    url(r'^student/profile/(?P<sapid>[0-9]+)/$',
        views.student_profile, name='student_profile'),
    url(r'^student/editprofile/(?P<sapid>[0-9]+)/$',
        views.student_editprofile, name='student_editprofile'),
    url(r'^notifications/$', views.notifs, name='notifs'),
    url(r'^search/$', views.student_list, name='student_list'),
    url(r'^teacherdashboard/$', views.teacher_dashboard),
]
