from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from datetime import datetime
import time
import queue

from tasks.queue_class import Queues
from tasks.stack_class import Stack
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

listTask = []
listTask_by_date = Task.objects.all().order_by("date")
listTrier = Task.objects.all().order_by("priority")

stack_task = Stack()
queue_task = Queues()


for item in listTask_by_date:
    queue_task.add_task(item)
    
for task in listTrier[::-1]:
    stack_task.add_task(task)


listTask = stack_task.get_all()





    

print('--------------------------')

for task in  stack_task.get_all():
    print(task.priority)

    
print('--------------------------')


for task in  queue_task.get_all():
    print(task.date)
    
print('--------------------------')

class TaskListView(ListView):
    model = Task
    context_object_name = 'listTask'
    

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
