from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=1028)
    priority = models.IntegerField()
    status = models.BooleanField()

    def __str__(self):
        return f("task: {self.title} priority: {self.priority} status: {self.status} ")