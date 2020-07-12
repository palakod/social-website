from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image

@receiver
def users_like_changed(m2m_changed, sender=Image.users_like.through):
    instance.total_likes = instance.users_like.count()
    instance.save()