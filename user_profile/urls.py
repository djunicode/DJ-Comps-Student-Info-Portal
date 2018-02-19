from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/student/$', views.register, name='register'),
    url(r'^login/student/$', views.user_login, name='login'),
    url(r'^register/teacher/$', views.register_teacher, name='register_teacher'),
    url(r'^login/teacher/$', views.user_login_teacher, name='user_login_teacher'),
    url(r'^logout/$', views.logout, name='logout'),
]
