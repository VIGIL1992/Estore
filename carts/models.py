from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
    
class CartItem(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    
    
    def sub_total(self):
        return self.product.price * self.quantity 
    # def __str__(self):
    #     return self.product
    
    def __unicode__(self):
        return self.product.name