import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import GalleryImage


@receiver(post_delete, sender=GalleryImage)
def delete_files(sender, instance, **kwargs):
    if instance.image:
        if os.path.exists(instance.image.path):
            os.remove(instance.image.path)  # Видалення основного зображення
    if instance.thumbnail:
        if os.path.exists(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)  # Видалення мініатюри
