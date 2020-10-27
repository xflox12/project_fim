from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField
    name = models.TextField()
    surname = models.TextField()
    email = models.TextField()
    email2 = models.TextField()
    info = models.TextField(default="this is a default info")
    age = models.TextField()

