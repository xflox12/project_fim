from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField
    name = models.TextField()
    surname = models.TextField()
    email = models.TextField()
    info = models.TextField(default="this is a default info")

