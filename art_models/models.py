from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True)


class ArtGallery(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    title = models.CharField()
    image = models.ImageField(upload_to='images_art')
    price = models.PositiveIntegerField()
    description = models.TextField()
    years_drown = models.DateField()
