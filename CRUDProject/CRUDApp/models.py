from django.db import models


class User(models.Model):
    name=models.CharField(max_length=500,  unique=True)
    email=models.EmailField( unique=True)
