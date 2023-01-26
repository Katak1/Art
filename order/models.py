from django.db import models
from django.contrib.auth import get_user_model

from art_models.models import ArtGallery

User = get_user_model()


class Order(models.Model):
    STATUS_CHOISES = (
        ('open', 'Открыт'),
        ('processing', 'В процессе'),
        ('closed', 'Закрыт')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers')
    art = models.ForeignKey(ArtGallery, on_delete=models.CASCADE, related_name='arts')
    status = models.CharField(max_length=10, choices=STATUS_CHOISES, default='open')
    order_date = models.DateTimeField(auto_now=True)