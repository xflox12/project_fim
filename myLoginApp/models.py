# import django.db

# Create your models here.
from django.db import models


# from django.contrib.admin import models


class User2(models.Model):
    user_id = models.AutoField
    name = models.TextField()
    surname = models.TextField()
    email = models.TextField()
    email2 = models.TextField()
    info = models.TextField(default="this is a default info")
    age = models.TextField()
    age2 = models.TextField()


class Favourites(models.Model):
    recipe_id = models.TextField()
    user_id = models.TextField()


# Create your models here.
class User(models.Model):
    ACTIVE = 'ACT'
    NEW = 'NEW'
    LOCKED = 'LOC'
    DELETED = 'DEL'
    LIST_OF_VALUES_STATUS = [
        (ACTIVE, 'Active'),
        (NEW, 'New'),
        (LOCKED, 'Locked'),
        (DELETED, 'Deleted')
    ]

    # PrimaryKey
    User_ID = models.BigAutoField(primary_key=True,
                                  verbose_name="Unique UserId"
                                  )

    # First Name with max 100 Characters
    Firstname = models.CharField(verbose_name="Firstname",
                                 max_length=100
                                 )

    # Last Name with max 100 Characters
    Surname = models.CharField(verbose_name="Surname",
                               max_length=100
                               )

    #    @property
    #    def full_name(self):
    #        "Returns the person's full name."
    #        return '%s %s' % (self.firstname, self.surname)

    # nickname is used to show on recipes and comments/ratings
    # not unique
    Nickname = models.CharField(verbose_name="Nickname",
                                max_length=100
                                )

    # Unique user identification - used for login
    Email = models.EmailField(verbose_name="EMail-Address",
                              max_length=300
                              )

    # picture is shown on recipes and comments/ratings (maybe it is necessary to add a very small size of the picture)
    Picture = models.ImageField(verbose_name="UserPicture"
                                )

    # ACT ... Active
    # NEW ... New - after registration an before confirmation (link sent via email)
    # LOC ... Locked after 3 login attempts
    # DEL ... Deleted - not used anymore (delete after X weeks of inactivity)
    Status = models.CharField(verbose_name="Status",
                              max_length=3,
                              choices=LIST_OF_VALUES_STATUS,
                              default=NEW
                              )

    # time of the last valid login of the user
    LastLogin = models.DateTimeField(verbose_name="Last Login Date"
                                     )

    # how often has the user tried to login (maybe with wrong password)
    # after 3 attempts the user-status is changed to LOC
    RetryLogin = models.PositiveSmallIntegerField(verbose_name="Number of Login Attempts"
                                                  )


class Recipe(models.Model):
    # primary key
    RecipeId = models.BigAutoField(primary_key=True,
                                   verbose_name="Unique RecipeId"
                                   )

    # Name/Title of the recipe
    RecipeName = models.CharField(verbose_name="Recipe Name",
                                  max_length=300
                                  )

    # only one picture per recipe
    Picture = models.ImageField(verbose_name="Recipe Picture"
                                )

    # Author is the user who created the recipe (UserID)
    UserId = models.ForeignKey(User,
                               verbose_name="Author",
                               on_delete=models.PROTECT
                               )

    # total calories
    Calories = models.PositiveIntegerField(verbose_name="Calories")

    # number of people suitable for the quantities in the recipe
    NumberPeople = models.PositiveSmallIntegerField(verbose_name="Number of People")


class Rating(models.Model):
    # primary key
    RatingId = models.BigAutoField(primary_key=True,
                                   verbose_name="Unique RatingId"
                                   )

    # Author is the user who created the comment and rating (UserID)
    UserId = models.ForeignKey(User,
                               verbose_name="Author",
                               on_delete=models.CASCADE
                               )

    # Comment can be added if wanted
    Comment = models.TextField(verbose_name="Comment",
                               blank="true")

    # 5Stars rating, 0.5 Stars possible (10 steps in total)
    # Do we have to set a max value? How can we do that?
    Scale = models.PositiveSmallIntegerField(verbose_name="Star Rating",
                                             default=0)

    # Date and Time the rating was created or modified
    DateTime = models.DateTimeField(verbose_name="Creation Date",
                                    auto_now="true")

    # Option to set comments invisible in case they are inappropriate or should not be visible for other reasons
    Visible = models.BooleanField(verbose_name="Visible",
                                  default="true")


class RecipeSteps(models.Model):
    # primary key
    RatingId = models.BigAutoField(primary_key=True,
                                   verbose_name="Unique RecipeStepId"
                                   )

    # Author is the user who created the comment and rating (UserID)
    RecipeId = models.ForeignKey(Recipe,
                                 verbose_name="Recipe",
                                 on_delete=models.PROTECT
                                 )

    # total amount of time required to cook recipe
    # how can we show it in minutes?
    Duration = models.PositiveSmallIntegerField(verbose_name="Duration")

    # order of steps
    StepNo = models.PositiveSmallIntegerField(verbose_name="Step Number")

    # Description of each step
    Description = models.TextField(verbose_name="Description")

    # If necessary, Tips can be added to the steps
    Tips = models.TextField(verbose_name="Tips")


class Folder(models.Model):
    # primary key
    FolderId = models.BigAutoField(primary_key=True,
                                   verbose_name="Unique FolderId"
                                   )

    #
    Name = models.CharField(verbose_name="Name",
                            max_length=200
                            )

    # necessary to sort favourites
    Position = models.PositiveSmallIntegerField(verbose_name="Position")

    FolderIdParent = models.ForeignKey('self',
                                       verbose_name="Parent Folder",
                                       on_delete=models.CASCADE
                                       )


class Favourite(models.Model):
    # primary key
    FavouriteId = models.BigAutoField(primary_key=True,
                                      verbose_name="Unique FavouriteId"
                                      )

    #
    UserId = models.ForeignKey(User,
                               verbose_name="Author",
                               on_delete=models.PROTECT
                               )

    #
    RecipeId = models.ForeignKey(Recipe,
                                 verbose_name="Recipe",
                                 on_delete=models.CASCADE
                                 )

    # FK Folder ist still missing!
    FolderId = models.ForeignKey(Folder,
                                 verbose_name="Folder",
                                 on_delete=models.CASCADE
                                 )

    # Note can be added if wanted
    Note = models.TextField(verbose_name="Note")

    # number of people wanted
    NumberPeople = models.PositiveSmallIntegerField(verbose_name="Number of People")

    # necessary to sort favourites
    Position = models.PositiveSmallIntegerField(verbose_name="Position")

