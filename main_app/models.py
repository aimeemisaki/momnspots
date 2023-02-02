from xmlrpc.client import DateTime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
# Category Choices
category_choices = [
    ('Deli', 'Deli'),
    ('Restaurant', 'Restaurant'),
    ('Apparel', 'Apparel'),
    ('Art Supplies', 'Art Supplies'),
    ('Beauty Supplies', 'Beauty Supplies'),
    ('Bookshop','Bookshop'),
    ('Drug Store', 'Drug Store'),
    ('Grocery Store', 'Grocery Store'),
    ('Plant Nursery','Plant Nursery'),
    ('Children Boutique', 'Children Boutique'),
    ('Other', 'Other'),
]

neighborhood_choices = [
    ('East and Northeast LA', 'East and Northeast LA'),
    ('Downtown LA', 'Downtown LA'),
    ('Echo Park and Westlake', 'Echo Park and Westlake'),
    ('Hollywood', 'Hollywood'),
    ('Harbor Area', 'Harbor Area'),
    ('Los Feliz and Silverlake', 'Los Feliz and Silverlake'),
    ('South Central', 'South Central'),
    ('San Fernando Valley', 'San Fernando Valley'),
    ('West LA', 'West LA'),
    ('Wilshire', 'Wilshire'),
]

class Post(models.Model):
    shop_name = models.CharField(max_length=200)
    img = models.FileField(
        validators=[FileExtensionValidator(['pdf', 'png', 'jpg', 'jpeg', 'webp', 'svg', 'heic'])])
    story = models.TextField(max_length=600)
    # created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=250, choices=category_choices)
    neighborhood = models.CharField(max_length=250, choices=neighborhood_choices)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop_name
    
    def get_absolute_url(self):
        return reverse('posts:detail', args=[self.id])

    class Meta:
        ordering = ['shop_name']

class Tag(models.Model):
    title = models.CharField(max_length=150)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.title