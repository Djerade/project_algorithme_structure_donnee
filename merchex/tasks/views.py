from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from datetime import datetime
import time
import queue
from queue import Queue

from tasks.stack_class import Stack
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

listTask = []
listTask = Task.objects.all().order_by("date")
listTrier = Task.objects.all().order_by("priority")

stack_task = Stack()

for task in listTrier[::-1]:
    stack_task.add_task(task)
    

listTask = stack_task.items
# print(type(stack_task.items))
    
    # print(x.priority)
# for task in listTrier:
#     # print(task.priority)
#     stack_task.add_task(task)




listObjet = []

    

print('--------------------------')
# for task in listTrier:
#     print(task.date)
for task in  listTask:
    objectTask = {}
    objectTask["id"]= task.id
    objectTask["title"]= task.title
    objectTask["description"]= task.description
    objectTask["category"]= task.category
    objectTask["date"]= task.date
    objectTask["priority"]= task.priority
    listObjet.append(objectTask)
    



for task in listTask:
      print(task)
    
    
print('--------------------------')


class TaskListView(ListView):
    model = Task
    context_object_name = 'listTask'
    
# class TaskListView(ListView):
#     model = Task
#     context_object_name = 'listTask'
#     queryset = stack_task.get_all()
#     template_name = "tasks/task_list.html"
    
    
class TaskDetailView(DetailView):
    model = Task

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:task_list')
