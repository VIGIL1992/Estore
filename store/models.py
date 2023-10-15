from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
#category
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'catagories'

#Customer or user details
# class Customer(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=10)
#     email = models.EmailField(max_length=100)
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
    
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


#Product details
class Product(models.Model):
    # id = models.AutoField(unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=500, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', blank=True, null=True)
    
    def __str__(self):
        return self.name


#Customer orders
# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     quantity = models.CharField(default=1, max_length=3)
#     address = models.CharField(max_length=100, default='', blank=True)
#     phone = models.CharField(max_length=10, blank=True)
#     date = models.DateField(default=datetime.datetime.today)
#     status = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.product


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
    

