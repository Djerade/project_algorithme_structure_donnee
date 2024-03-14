from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from datetime import datetime
import time
import queue
from queue import Queue
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

listTask = []
listTask = Task.objects.all()


    

print('--------------------------')
for task in  listTask:
    objectTask = {}
    objectTask["i"]= task.id
    objectTask["title"]= task.title
    objectTask["description"]= task.description
    objectTask["category"]= task.category
    objectTask["date"]= task.date
    objectTask["priority"]= task.priority



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
