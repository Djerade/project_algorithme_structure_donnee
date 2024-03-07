#-*- coding:utf-8 -*-
from .models import Category, Priority, Task
from django import forms

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"



# class  TaskForm(forms.Form):
#     title = forms.CharField(label="titre", max_length=65)
#     description = forms.CharField(label="description", max_length=100)
#     priority = forms.CharField(label="priorité", max_length=1)
#     category = forms.CharField(label="Categorie", max_length=5)
#     date = forms.CharField(label="Date d'écheance", max_length=100)
