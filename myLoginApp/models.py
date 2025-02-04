from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    UserId = models.OneToOneField(User, on_delete=models.CASCADE)

    # picture is shown on recipes and comments/ratings (maybe it is necessary to add a very small size of the picture)
    Picture = models.ImageField(verbose_name="Profile Picture",
                                blank=True,
                                upload_to="upload/"
                                )

    def __str__(self):  # to make it more readable in the admin panel (shows name instead of PK)
        return self.UserId.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(UserId=instance)
    instance.profile.save()
