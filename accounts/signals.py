from django.db.models.signals import post_save  # this signal is fired after an object is saved
from django.contrib.auth.models import User  # here User model is sending the signal
from django.dispatch import receiver
from .models import Profile

# user sends the signal post_save to the function create_profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
