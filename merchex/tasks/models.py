from django.db import models
import datetime

# Create your models here.

class Priority(models.TextChoices):
    VERY_IMPORTANT = 'v', "très important"
    LESS= 'm', "moins"
    IMPORTAN = 'i', "Important"
    
    
class Category(models.TextChoices):
    PROFESSIONEL = 'pr', "Professionel"
    PERSONNEL= 'P', "Personnel"
    SOCIAL = 's', "Social"

class Task(models.Model):
    title = models.CharField(verbose_name="titre", max_length=65, unique=True)
    description = models.CharField(verbose_name="description", max_length=100)
    priority = models.CharField(verbose_name="priorité", max_length=1, choices=Priority.choices)
    category = models.CharField(verbose_name="Categorie", max_length=5, choices=Category.choices)
    date = models.CharField(verbose_name="Date d'écheance", max_length=100)

    def __str__(self):
        return self.title
