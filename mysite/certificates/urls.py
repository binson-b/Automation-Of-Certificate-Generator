from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views
urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^login/', views.login, name="login"),
    url(r'^verify/', views.verify, name='verify'),
    url(r'^preview',views.preview, name='preview'),
    url(r'^logout/$',views.logout_user , name="logout"),
    url(r'^register/$',views.register, name='register'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile/$',views.profile, name='profile'),

    url(r'^home/change_password/$', views.change_password, name='change_password'),

    url(r'^home/add_user/$', views.add_user_profile, name='add_user_profile'),
    url(r'^home/edit_user/$', views.edit_user_profile, name="edit_user"),
    url(r'^home/view_user/$', views.view_user_profile, name="view_user_profile"),
    url(r'^home/delete_user/$', views.delete_user_profile, name="delete_user_profile"),

    url(r'^home/add_certificate/$', views.add_certificate, name="add_certificate"),
    url(r'^home/edit_certificate/$', views.edit_certificate, name="edit_certificate"),
    url(r'^home/view_certificate/$', views.view_certificate, name="view_certificate"),
    url(r'^home/delete_certificate/$', views.delete_certificate, name="delete_certificate"),

    url(r'^home/send_certificate/$', views.send_certificate, name="send_certificate"),
    url(r'^home/show_participant/$', views.show_participant, name="show_participant"),
    url(r'^home/send_email/$', views.send_email, name="send_email"),

    url(r'^home/add_event/$', views.add_event, name="add_event"),
    url(r'^home/edit_event/$', views.edit_event, name="edit_event"),
    url(r'^home/view_event/$', views.view_event, name="view_event"),
    url(r'^home/delete_event/$', views.delete_event, name="delete_event"),

    url(r'^home/organise_event/$', views.organise_event, name="organise_event"),
    url(r'^home/edit_organised_event/$', views.edit_organised_event, name="edit_organised_event"),
    url(r'^home/view_organised_event/$', views.view_organised_event, name="view_organised_event"),
    url(r'^home/delete_organised_event/$', views.delete_organised_event, name="delete_organised_event"),
]