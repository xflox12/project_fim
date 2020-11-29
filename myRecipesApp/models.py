from django.db import models

# Create your models here.
from myLoginApp.models import User
from myUnitsApp.models import Unit


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
                                   max_digits=8,  # before none
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
