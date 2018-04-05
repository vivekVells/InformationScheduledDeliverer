from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('schedule', views.schedule, name='schedule'),
    path('stopschedule', views.stopschedule, name='stopschedule'),
]