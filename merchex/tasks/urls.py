#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('', views.TaskListView.as_view(), name='task_list'),
    path('filter_priority/', views.TaskListViewPriority.as_view(), name='task_list_priority'),
    path('filter_date/', views.TaskListViewDate.as_view(), name='task_list_date'),
    re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name= 'task_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete')
]

