from django.db import models

# Create your models here.
class NewsletterUser(models.Model):
    email = models.EmailField() # checks if the email address is formatted correctly
    date_added =  models.DateTimeField(auto_now_add=True)  # captures the exact time a person signed up for the newsletter for spam complains purposes

    def __str__(self):
        return self.email