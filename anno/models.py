from django.db import models

# Create your models here.
class SearchResult(models.Model):
    query = models.CharField(max_length=100)
    rank = models.IntegerField()
    content = models.CharField(max_length=2000)


