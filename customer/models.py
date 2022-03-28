from django.db import models
from django.contrib.auth.models import User
from owner.models import Books

# Create your models here.

# carts item,user,date,status
# model relationships
# one to one
# one to many
class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Books,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    options=(
        ('incart','incart'),
        ('cancelled','cancelled'),
        ('orderplaced','orderplaced')

    )
    status=models.CharField(max_length=120,choices=options,default='incart')
class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Books,on_delete=models.CASCADE)
    delivery_address=models.CharField(max_length=200)
    phone=models.CharField(max_length=15)
    date=models.DateField(auto_now_add=True)
    options=(
        ('order_placed','order_placed'),
        ('dispatched','dispatched'),
        ('intransit','intransit'),
        ('delivered','delivered'),
        ('cancelled','cancelled')
    )
    status=models.CharField(max_length=120,choices=options,default='order_placed')