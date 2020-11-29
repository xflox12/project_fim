from django.db import models

from myLoginApp.models import User
from myRecipesApp.models import Recipe


# Create your models here.
class Folder(models.Model):
    # primary key
    FolderId = models.BigAutoField(primary_key=True,
                                   verbose_name="Unique FolderId"
                                   )

    # Name of the folder
    Name = models.CharField(verbose_name="Name",
                            max_length=200
                            )

    # The Position is necessary to sort favourites
    Position = models.PositiveSmallIntegerField(verbose_name="Position")

    # Parent Folder (Path)
    FolderIdParent = models.ForeignKey('self',
                                       verbose_name="Parent Folder",
                                       on_delete=models.CASCADE
                                       )


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

    #
    FolderId = models.ForeignKey(Folder,
                                 verbose_name="Folder",
                                 on_delete=models.SET(1)   # before models.SET_NULL
                                 )

    # Note can be added if wanted
    Note = models.TextField(verbose_name="Note")

    # number of people wanted
    # conversion to the required number of people
    NumberPeople = models.PositiveSmallIntegerField(verbose_name="Number of People")

    # necessary to sort favourites
    Position = models.PositiveSmallIntegerField(verbose_name="Position")
