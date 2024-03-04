from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from todolist.models import Task

def home(request):
    tasks = Task.objects.all()
    print(tasks)
    # template = loader.get_template('index.html')
    return HttpResponse(f"""
                         <h1>Task !</h1>
                         <p>Nos tasks de la journée<p>
                         <ul>
                             <li>{tasks[0].name_task}</li>
                          </ul>
                        """)