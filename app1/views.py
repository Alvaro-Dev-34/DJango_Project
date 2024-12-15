from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404


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
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })
    # return render(projects_all, safe=False)


def tasks(request):
    #task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })
    # return render('task: %s' % task.title)
