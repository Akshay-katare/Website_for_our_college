from django.db import models


class Doubts(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)
    desc = models.TextField()

# Create your models here.
