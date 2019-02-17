from datetime import timezone

from django.db import models

# Create your models here.

class List(models.Model):

    title = models.CharField(
        max_length=30
    )

    content = models.TextField(
        null=True
    )

    date = models.CharField(
        max_length=30
    )

    finished = models.BooleanField(
        default= 0
    )




