from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        if not Customer.objects.filter(user=instance).exists():
            Customer.objects.create(user=instance, name=instance.username, email=instance.email)

@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    if hasattr(instance, 'customer'):
        instance.customer.save()
