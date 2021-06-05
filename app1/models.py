from django.db import models

# Create your models here.

class DTModel(models.Model):
    name = models.CharField(max_length=64, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    date_time = models.DateTimeField(null=True)