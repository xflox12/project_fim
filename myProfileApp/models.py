from django.db import models

from myLoginApp.models import User
from myRecipeApp.models import Recipe


# Create your models here.

class Favourite(models.Model):
    # primary key
    FavouriteId = models.BigAutoField(primary_key=True,
                                      verbose_name="Unique FavouriteId"
                                      )

    # Owner of the Favourite (UserID)
    UserId = models.ForeignKey(User,
                               verbose_name="Owner",
                               on_delete=models.PROTECT
                               )

    # Recipe behind the favourite
    RecipeId = models.ForeignKey(Recipe,
                                 verbose_name="Recipe",
                                 on_delete=models.CASCADE
                                 )

    # Note can be added if wanted
    Note = models.TextField(verbose_name="Note",
                            blank=True)

    # number of people wanted
    # conversion to the required number of people
    NumberPeople = models.PositiveSmallIntegerField(verbose_name="Number of People",
                                                    blank=True,
                                                    null=True)
