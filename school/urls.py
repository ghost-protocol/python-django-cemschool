from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    # login
    url(r'^login/$', auth_views.login, name='login'),
    # logout
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    # url(r'^logout/$', auth_views.logout, name='logout'),

	# homepage
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    # list students
    url(r'^students/$', views.student_list, name='student_list'),
    # create student
    url(r'^students/create/$', views.student_create, name='student_create'),
    # update student: Ex. students/5/update
    url(r'^students/(?P<pk>\d+)/update/$', views.student_update, name='student_update'),
    # delete student: Ex. students/5/delete
    url(r'^students/(?P<pk>\d+)/delete/$', views.student_delete, name='student_delete'),

    # list parents
    url(r'^parents/$', views.parent_list, name='parent_list'),
    # create parent
    url(r'^parents/create/$', views.parent_create, name='parent_create'),

    url(r'^parents/(?P<pk>\d+)/update/$', views.parent_update, name='parent_update'),

    url(r'^parents/(?P<pk>\d+)/delete/$', views.parent_delete, name='parent_delete'),

    # list medicals
    url(r'^medicals/$', views.medical_list, name='medical_list'),
    # create medical
    url(r'^medicals/create/$', views.medical_create, name='medical_create'),

    url(r'^medicals/(?P<pk>\d+)/update/$', views.medical_update, name='medical_update'),

    url(r'^medicals/(?P<pk>\d+)/delete/$', views.medical_delete, name='medical_delete'),

]