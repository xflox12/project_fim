from django.db import models
from django.urls import reverse

# Create your models here.
class Testmodel(models.Model):
    title = models.TextField()
    description = models.TextField()

    def get_absolute_url(self):
        return f"/testmodel/{self.id}"
        #return reverse ("link-to-home-model", kwargs={"my_id" : self.id})  #->add name to URL
