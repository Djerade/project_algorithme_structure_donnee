# Generated by Django 5.0.2 on 2024-03-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='descrioption', max_length=100, verbose_name='Task description'),
            preserve_default=False,
        ),
    ]
