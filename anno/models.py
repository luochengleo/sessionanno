from django.db import models

# Create your models here.

# MongoEngine	Django
# StringField	CharField
# URLField	URLField
# EmailField	EmailField
# IntField	IntegerField
# FloatField	FloatField
# DecimalField	DecimalField
# BooleanField	BooleanField
# DateTimeField	DateTimeField
# EmbeddedDocumentField	--
# DictField	--
# ListField	--
# SortedListField	--
# BinaryField	--
# ObjectIdField	--
# FileField	FileField
class Task(models.Model):
    content = models.CharField(max_length=1000)
    task_id = models.IntegerField()
    init_query = models.CharField(max_length=1000)

class Query(models.Model):
    content = models.CharField(max_length=100)
    task = models.ManyToManyField(Task)

class SearchResult(models.Model):
    # query = models.ForeignKey(Query)
    query = models.CharField(max_length=100)
    rank = models.IntegerField()
    content = models.CharField(max_length=2000)

class SingleChoiceQuestion(models.Model):
    description = models.CharField(max_length=1000)
    choices = models.CharField(max_length=5000)
    answer = models.IntegerField()
    task = models.ManyToManyField(Task)

class FillingQuestion(models.Model):
    description = models.CharField(max_length=1000)
    task = models.ManyToManyField(Task)


if __name__ == '__main__':
    task = Task(connect='hello world', task_id=0)
    task.save()






