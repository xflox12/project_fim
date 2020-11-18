# import django.db

from django.db import models
# from django.contrib.admin import models


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
    UserId = models.BigAutoField(primary_key=True,
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

    # How can we set constraints for the password?
    Password = models.CharField(verbose_name="Password",
                                max_length=50
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


class Unit(models.Model):
    # primary key
    UnitId = models.BigAutoField(primary_key=True,
                                 verbose_name="Unique UnitId"
                                 )

    # Name of the Unit e.g. Kilogram
    Name = models.CharField(verbose_name="Name",
                            max_length=200
                            )

    # Unit abbreviation e.g. kg
    # open: has to be unique!
    Abbreviation = models.CharField(verbose_name="Abbreviation",
                                    max_length=3
                                    )

    #
    # Conversion =


class FoodItem(models.Model):
    # primary key
    FoodItemId = models.BigAutoField(primary_key=True,
                                     verbose_name="Unique FoodItemId"
                                     )

    # Name of the Food Item e.g. Milk
    Name = models.CharField(verbose_name="Name",
                            max_length=200
                            )


class Category(models.Model):
    # primary key
    CategoryId = models.BigAutoField(primary_key=True,
                                     verbose_name="Unique CategoryId"
                                     )

    # Name of the category e.g. Dessert
    Name = models.CharField(verbose_name="Name",
                            max_length=200
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
    # open: should it be possible to set user Null after deleting or default user (better?)?; hint: DSGVO
    UserId = models.ForeignKey(User,
                               verbose_name="Author",
                               on_delete=models.PROTECT
                               )

    # total energy of given quantities
    Energy = models.PositiveIntegerField(verbose_name="Calories")

    # Unit for energy e.g. calories
    UnitId = models.ForeignKey(Unit,
                               verbose_name="Unit of Energy",
                               on_delete=models.PROTECT
                               )

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

    # Comment can be added voluntarily
    Comment = models.TextField(verbose_name="Comment",
                               blank=True)

    # 5-Stars rating (10 steps in total)
    # blank is no rating, 0 = 0 Stars rating, 1 = 0.5 Stars rating
    # open: Do we have to set a max value? How can we do that?
    Scale = models.PositiveSmallIntegerField(verbose_name="Star Rating",
                                             blank=True
                                             )

    # Date and Time the rating was created or modified
    DateTime = models.DateTimeField(verbose_name="Creation Date",
                                    auto_now=True)

    # Option to set comments invisible in case they are inappropriate or should not be visible for other reasons
    Visible = models.BooleanField(verbose_name="Visible",
                                  default=True)


class RecipeSteps(models.Model):
    # primary key
    RatingId = models.BigAutoField(primary_key=True,
                                   verbose_name="Unique RecipeStepId"
                                   )

    # Recipe the Recipe Steps are referring to (RecipeId)
    RecipeId = models.ForeignKey(Recipe,
                                 verbose_name="Recipe",
                                 on_delete=models.CASCADE
                                 )

    # total amount of time required to cook recipe (not broken down to single steps)
    # how can we show it in minutes?
    Duration = models.PositiveSmallIntegerField(verbose_name="Duration in Minutes",
                                                default=0
                                                )

    # order of steps
    StepNo = models.PositiveSmallIntegerField(verbose_name="Step Number")

    # Description of each step
    Description = models.TextField(verbose_name="Description")

    # If necessary, Tips can be added to the steps
    Tips = models.TextField(verbose_name="Tips",
                            blank=True
                            )


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
                                 on_delete=models.SET(1)   #before models.SET_NULL
                                 )

    # Note can be added if wanted
    Note = models.TextField(verbose_name="Note")

    # number of people wanted
    # conversion to the required number of people
    NumberPeople = models.PositiveSmallIntegerField(verbose_name="Number of People")

    # necessary to sort favourites
    Position = models.PositiveSmallIntegerField(verbose_name="Position")


class RecipeCategory(models.Model):
    # primary key
    RecipeCategoryId = models.BigAutoField(primary_key=True,
                                           verbose_name="Unique RecipeCategoryId"
                                           )

    # Author is the user who created Relationship (UserID)
    # open: check "protect2 -> what do we want to happen?
    UserId = models.ForeignKey(User,
                               verbose_name="Author",
                               on_delete=models.PROTECT
                               )

    # Recipe behind the favourite
    RecipeId = models.ForeignKey(Recipe,
                                 verbose_name="Recipe",
                                 on_delete=models.CASCADE
                                 )

    # Recipe behind the favourite
    CategoryId = models.ForeignKey(Category,
                                   verbose_name="Category",
                                   on_delete=models.CASCADE
                                   )


class Ingredient(models.Model):
    # primary key
    IngredientId = models.BigAutoField(primary_key=True,
                                       verbose_name="Unique UnitId"
                                       )

    Quantity = models.DecimalField(verbose_name="Quantity",
                                   max_digits=8, #before none
                                   decimal_places=2
                                   )

    UnitId = models.ForeignKey(Unit,
                               verbose_name="Unit",
                               on_delete=models.CASCADE
                               )

    FoodItemId = models.ForeignKey(FoodItem,
                                   verbose_name="Food Item",
                                   on_delete=models.CASCADE
                                   )

    # Note can be added if wanted
    Note = models.TextField(verbose_name="Note")
