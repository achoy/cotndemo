from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=256)
    address_2 = models.CharField(max_length=256)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=12)
    phone_1 = models.CharField(max_length=30)
    email_1 = models.EmailField(max_length=254)
    comments = models.TextField()
        
class UserReg(models.Model):
    user = models.ForeignKey(User)
    reg_date = models.DateTimeField('registration date')
    paid_date = models.DateTimeField('paid date')
    paid_amount = models.DecimalField(max_digits=8,decimal_places=2)
    
class Membership(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    year = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    
class Catalog(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    year = models.IntegerField()

  