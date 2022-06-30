from .models import Donor
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def post_save_create_donor(sender, instance, created, **kwargs):
    if created:
        Donor.objects.create(user=instance)

