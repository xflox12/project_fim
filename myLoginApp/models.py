import django.db

# Create your models here.
from django.db import models
#from django.contrib.admin import models



class User2(models.Model):
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
    user_id = models.BigAutoField(primary_key=True
                                  , verbose_name="Unique UserId"
                                  )

    # First Name with max 100 Characters
    firstname = models.CharField(verbose_name="Firstname"
                                 , max_length=100
                                 )

    # Last Name with max 100 Characters
    surname = models.CharField(verbose_name="Surname"
                               , max_length=100
                               )

    #    @property
    #    def full_name(self):
    #        "Returns the person's full name."
    #        return '%s %s' % (self.firstname, self.surname)

    # nickname is used to show on recipes and comments/ratings
    # not unique
    nickname = models.CharField(verbose_name="Nickname"
                                , max_length=100
                                )

    # Unique user identification - used for login
    email = models.EmailField(verbose_name="EMail-Address"
                              , max_length=300
                              )

    # picture is shown on recipes and comments/ratings (maybe it is necessary to add a very small size of the picture)
    picture = models.ImageField(verbose_name="Userpicture"
                                )

    # ACT ... Activ
    # NEW ... New - after registration an before confirmation (link sent via email)
    # LOC ... Locked after 3 login attempts
    # DEL ... Deleted - not used anymore (delete after X weeks of inactivity)
    status = models.CharField(verbose_name="Status"
                              , max_length=3
                              , choices=LIST_OF_VALUES_STATUS
                              , default=NEW
                              )

    # time of the last valid login of the user
    lastlogin = models.DateTimeField(verbose_name="Last Login Date"
                                     )

    # how often has the user tried to login (maybe with wrong password) - after 3 attempts the user-status is changed to LOC
    retrylogin = models.PositiveSmallIntegerField(verbose_name="Number of Login Attempts"
                                                  )
