# import django.db

# Create your models here.
from django.db import models
# from django.contrib.admin import models


class User2(models.Model):
    user_id = models.AutoField
    name = models.CharField(max_length=100)
    surname = models.TextField(blank=True)
    email = models.TextField()
    email2 = models.TextField()
    info = models.TextField(default="this is a default info")
    age = models.DecimalField(max_digits=3, decimal_places=0)
    age2 = models.TextField()

    def get_absolut_url(self):
       return f"/users/{self.id}"

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
