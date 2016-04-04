from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import *
from django.db import models
from tasks.models import Task, User
from splash.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



from django.template import loader, Context

def main(request):
    #task generation

    all_tasks = Task.objects.all()
    current_user = request.user
    tasks = []
    collabtasks = []
    collabtasks.append(Task.objects.filter(collaborators=current_user))

    for task in all_tasks:
        if task.owner == current_user:
            tasks.append(task)
    if current_user.is_authenticated():
        context = {'tasks': tasks}
        return render(request, "main.html", {'context': context})
    else:
        return HttpResponseRedirect('/')


def addTask(request):
    
    #concatenates tasks to task inex

    if request.method == 'POST':
        user = request.user
        owner = user
        title = request.POST['title']
        description = request.POST['description']
        isComplete = False
        task = Task(owner = owner, title = title, description = description, isComplete=False)
        collaborators = [request.POST['collaborator1'], request.POST['collaborator2'], request.POST['collaborator3']]
        for collab in collaborators:
            collab.lower()

        if task is not None:
            task.save()
            return HttpResponseRedirect('/tasks/')
        else:
            return render(request, 'tasks/main.html', {'errors':"Make sure you fill in all the fields!"})

        for collab in collaborators:
            partner = User.objects.get(email = collab)
            coll_add = task.collaborators.add(partner)
            coll_add.save()

def removeTask(request, task_id):
    task_id = int(task_id)
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect('/tasks')

def toggle(request, task_id):
    task_id = int(task_id)

    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        if task.isComplete == True:
            task.isComplete = False
        else:
            task.isComplete = True

        task.save();
    return HttpResponseRedirect('/tasks')
