from django.db import models

# Create your models here.
class order(models.Model):
    id = models.IntegerField(max_length=60, unique=True)
    api_version = models.IntegerField(max_length=60, unique=False)
    type = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    missed_reason = models.CharField(max_length=100, null=True)
    persons = models.IntegerField