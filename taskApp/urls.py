from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('projects/', views.projects, name='projects'),
]