from django.db import models
import datetime

# Create your models here.

class Priority(models.TextChoices):
    VERY_IMPORTANT = 'v', "élévée"
    IMPORTANT = 'i', "moyenne"
    LESS= 'l', "faible"
    
    
class Category(models.TextChoices):
    PROFESSIONEL = 'pr', "Professionel"
    PERSONNEL= 'p', "Personnel"
    SOCIAL = 's', "Social"


class Task(models.Model):
    title = models.CharField(verbose_name="titre", max_length=65, unique=True)
    description = models.CharField(verbose_name="description", max_length=100)
    priority = models.CharField(verbose_name="priorité", max_length=1, choices=Priority.choices)
    category = models.CharField(verbose_name="Categorie", max_length=5, choices=Category.choices)
    date = models.DateField(verbose_name="Date d'échéance", default=datetime.date.today)

    def __str__(self):
        return self.title+"  "+ self.description +"  " + self.priority +"  "
    
