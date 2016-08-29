from django.conf.urls import url
from gait_analysis_service.user_management import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^register/$', views.register),
    url(r'^login/$', views.userLogin),
    url(r'^logout/$', views.userLogout),

    url(r'^checkusername/$', views.checkUsername),
    url(r'^userprofile/$', views.modify),

    url(r'^mregister$', views.userRegister_mobile),
    url(r'^mlogin$', views.userLogin_mobile),
    url(r'^mlogout$', views.userLogout_mobile),
    url(r'^minfo$', views.queryInformation_mobile),
    url(r'^mmodifyInformation$', views.modifyInformation_mobile),
    url(r'^mmodifyPassword$', views.modifyPassword_mobile),

    url(r'^modifyPassword/$', views.modifyPassword),
    url(r'^modifyInformation/$', views.modifyInformation),
]
