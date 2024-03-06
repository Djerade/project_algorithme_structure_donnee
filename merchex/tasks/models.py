from django.db import models


# Create your models here.

class Priority(models.TextChoices):
    VERY_IMPORTANT = 'v', "important"
    LESS= 'm', "moins"
    IMPORTAN = 'i', "Important"
    

class Task(models.Model):
    title = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    description = models.CharField(verbose_name="Task description", max_length=100)
    priority = models.CharField(verbose_name="Task description", max_length=1, choices=Priority.choices)
    date = models.CharField(max_length=65)
    category = models.CharField(max_length=65)

    def __str__(self):
        return self.name
