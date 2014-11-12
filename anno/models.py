from django.db import models

# Create your models here.

class Task(models.Model):
    content = models.CharField(max_length=1000)
    task_id = models.IntegerField()


class Query(models.Model):
    content = models.CharField(max_length=100)
    task = models.ManyToManyField(Task)


class SearchResult(models.Model):
    query = models.ForeignKey(Query)
    rank = models.IntegerField()
    content = models.CharField(max_length=2000)


class SingleChoiceQuestion:
    description = models.CharField(max_length=1000)
    choices = models.CharField(max_length=5000)
    answer = models.IntegerField()
    task = models.ManyToManyField(Task)


class FillingQuestion:
    description = models.CharField(max_length=1000)
    task = models.ManyToManyField(Task)







