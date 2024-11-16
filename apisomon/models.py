from django.db import models
from django.contrib.auth.models import AbstractUser

class CastumorUser(AbstractUser):
    pass

class Category(models.Model):
    name_category = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name_category
    

class Product(models.Model):
    user_id = models.ForeignKey(CastumorUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_name = models.CharField(max_length=50)
    date_post = models.DateTimeField(auto_now=True, auto_now_add=False)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    phone = models.CharField(max_length=13)
    location = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.product_name
    



