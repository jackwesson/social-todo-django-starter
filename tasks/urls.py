from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^addTask/', views.addTask, name='addTask'),
    url(r'^removeTask/([0-9]+)', views.removeTask, name='removeTask'),
    url(r'^toggle/([0-9]+)', views.toggle, name='toggle'),
]
