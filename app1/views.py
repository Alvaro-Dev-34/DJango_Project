from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject


# Create your views here.

def index(request):
    title = "Django Course!!"
    return render(request, "index.html", {
        "title": title
    })


def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)


def about(request):
    username = "Sofia"
    return render(request, "about.html", {
        'username': username
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
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            projects_id=2)
        return redirect(
            'tasks')  # esta redireccion  es usando el nombre que le he dado a la url (como si fuera una variable)


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
