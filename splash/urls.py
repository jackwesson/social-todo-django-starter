from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^login_form/$', views.login_form, name = 'login_form'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^logout_form/$', views.logout_form, name = 'logout_form'),


]
