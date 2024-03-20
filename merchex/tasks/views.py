from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from datetime import datetime
import time
import queue
from queue import Queue

from tasks.queue_class import Queues
from tasks.stack_class import Stack
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

listTask = Task.objects.all()
listTaskDate = Task.objects.all().order_by("date")
listTaskPriority = Task.objects.all().order_by("priority")

queue_task = Queues()
stack_task = Stack()

for task  in  listTaskDate:
    queue_task.add_task(task)

for task in listTaskPriority[::-1]:
    stack_task.add_task(task)
    

# listTask = stack_task.items
# print(type(stack_task.items))
    
    # print(x.priority)
# for task in listTrier:
#     # print(task.priority)
#     stack_task.add_task(task)



listObjet = []

    

print('--------------------------')
# for task in listTrier:
#     print(task.date)
# for task in  listTask:
#     objectTask = {}
#     objectTask["id"]= task.id
#     objectTask["title"]= task.title
#     objectTask["description"]= task.description
#     objectTask["category"]= task.category
#     objectTask["date"]= task.date
#     objectTask["priority"]= task.priority
#     listObjet.append(objectTask)
    



for task in queue_task.get_all():
      print(task)
    
    
print('--------------------------')


class TaskListView(ListView):
    model = Task
    context_object_name = 'listTask'
    
class TaskListViewPriority(ListView):
    model = Task
    context_object_name = 'listTask'
    queryset = stack_task.get_all()
    template_name = "tasks/sort/task_list_priority.html"
    
    
class TaskListViewDate(ListView):
    model = Task
    context_object_name = 'listTask'
    queryset = queue_task.get_all()
    template_name = "tasks/sort/task_list_date.html"
    
    
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
    queue_task.delete_task()
    success_url = reverse_lazy('tasks:task_list')
