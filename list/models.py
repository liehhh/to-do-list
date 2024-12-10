from django.db import models
from django.utils import timezone


class List(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateField()
