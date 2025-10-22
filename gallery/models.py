from django.dispatch import receiver
from django.db import models
import os
from PIL import Image
from django.db.models.signals import post_delete


class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    thumbnail = models.ImageField(upload_to='gallery/thumbnails/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_created=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.create_thumbnail()

    def create_thumbnail(self):
        img_path = self.image.path
        thumb_path = os.path.join(os.path.dirname(img_path), "thumbnails", os.path.basename(img_path))
        img = Image.open(img_path)
        img.thumbnail((200, 200))
        os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
        img.save(thumb_path)
        self.thumbnail = f"gallery/thumbnails/{os.path.basename(img_path)}"
        super().save(update_fields=['thumbnail'])

    def __str__(self):
        return self.title



