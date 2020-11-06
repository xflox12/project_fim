import django.db

# Create your models here.
class User(models.Model):
    user_id = models.AutoField
    name = models.TextField()
    surname = models.TextField()
    email = models.TextField()
    email2 = models.TextField()
    info = models.TextField(default="this is a default info")
    age = models.TextField()

class Favourites(models.Model):
    receipe_id = models.TextField()
    user_id = models.TextField()

