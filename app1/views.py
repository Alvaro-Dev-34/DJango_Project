from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject, DeleteProject, DeleteTask


# Create your views here.

def index(request):
    title = "Django Project!!"
    return render(request, "index.html", {
        "title": title
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })
    # return render(projects_all, safe=False)


def tasks(request):
    # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })
    # return render('task: %s' % task.title)


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        project = get_object_or_404(Project, name=request.POST["project_name"])

        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            projects_id=project.id)
        return redirect('tasks')
                    # esta redireccion  es usando el nombre que le he dado a la url (como si fuera una variable)


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        print(request.POST)
        project = Project.objects.create(name=request.POST["name"])
        print(project)
        return redirect('projects')


def project_detail(request, id):
    print(id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(projects_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })


def delete_project(request):
    if request.method == 'POST':
        print(request.POST)
        project_to_delete = get_object_or_404(Project, name=request.POST["name"])
        project_to_delete.delete()
        print("Eliminado: " + request.POST["name"])
        return redirect('delete_project')
    else:
        return render(request, 'projects/delete_project.html', {
            'form': DeleteProject()
        })


def delete_task(request):
    if request.method == 'POST':
        print("holi")
        print(request.POST)
        print("1")
        task_to_delete = get_object_or_404(Task, title=request.POST["title"])
        print("2")
        task_to_delete.delete()
        print("Eliminada: " + request.POST["title"])
        return redirect('delete_task')
    else:
        return render(request, 'tasks/delete_task.html', {
            'form': DeleteTask()
        })