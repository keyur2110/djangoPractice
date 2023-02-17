from django.db import models
# Create your models here.

class login_data(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{login_data.username} {login_data.password}"

class user_data(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Contact = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)
    
    def __str__(self):
        return f"{user_data.Name} {user_data.Contact} {user_data.id}"
    
class product_data(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{product_data.product_name} {product_data.price} {product_data.quantity}"
