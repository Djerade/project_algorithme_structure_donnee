from django.db import models

# Create your models here.
class Task(models.Model):
    name_task = models.fields.CharField(max_length=100)