from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class CategoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class ProductModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(default=None, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return str(self.id)

class CommentModel(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.content