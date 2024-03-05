from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from todolist.models import Task

def home(request):
    tasks = Task.objects.all()
    print(tasks)
    # template = loader.get_template('index.html')
    return render(request, 'index.html')