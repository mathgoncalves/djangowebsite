from django.db import models

class Publication (models.Model):
    title = models.CharField(max_length=200)
    preview_description = models.TextField()
    description = models.TextField()
    external_articles = models.TextField()
    image = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Create your models here.
