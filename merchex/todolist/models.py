from django.db import models

# Create your models here.
class Task(models.Model):
    name_task = models.fields.CharField(max_length=100)
    description_task = models.fields.CharField(max_length=500)
    priority_task = models.fields.CharField(max_length=100)
    date_task = models.fields.CharField(max_length=100)
    category_task = models.fields.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return self.name_task