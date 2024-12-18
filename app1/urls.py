
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('create_project/', views.create_project, name="create_project"),
    path('delete_project/', views.delete_project, name="delete_project"),

    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('delete_task/', views.delete_task, name="delete_task"),

]