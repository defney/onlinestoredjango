from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #portfolio_site = models.URLField(blank=True)
    #profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #email =  models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    address =  models.CharField(max_length=100, null=True, blank=True)
    city =  models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.user.username


class productcategories (models.Model):
    # STATUS = (
    #     (1,'True'),
    #     (0,'False'),
    # )
    CategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryName



# Create your models here.
class products (models.Model):
    # STATUS = (
    #     (1,'True'),
    #     (0,'False'),
    # )
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    CategoryID = models.ForeignKey(productcategories,on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    Quantity = models.CharField(max_length=100)
    ShortDesc = models.CharField(max_length=100)
    LongDesc = models.CharField(max_length=100)
    image=models.ImageField(upload_to= 'foods')
    stock = models.FloatField(max_length=100)
    Location = models.CharField(max_length=100)
    changedprice = models.FloatField()
    commented = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name



class cartItem(models.Model):
    itemID = models.AutoField(primary_key=True)
    product = models.OneToOneField(products, on_delete=models.SET_NULL, null=True)
    itemquantity = models.IntegerField(default=1)#how much is added to the cart
    date_added = models.DateTimeField(auto_now=True)
    itemPrice = models.FloatField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    totalCost = models.FloatField(max_length=100,default=0)

    def set_itemPrice(self):
        self.itemPrice = (self.itemquantity)*(self.product.changedprice)
        return self.itemPrice

    def get_cart_total(self):
        self.totalCost = sum(self.all().itemPrice)
        return self.totalCost

    def __str__(self):
        return 'cartItem: {}'.format(self.product)




class orders (models.Model):
    orderID = models.AutoField(primary_key=True)
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
    )
    details = models.ForeignKey(cartItem, null=True, on_delete=models.SET_NULL)
    status = models.CharField(choices=STATUS, max_length=160, default='New')
    date_created = models.DateTimeField(auto_now_add=True)

    def return_date_due():
        now = timezone.now()
        return now + timedelta(days=7)
    
    date_due = models.DateTimeField(default=return_date_due)

    def __str__(self):
        return 'orders: {}'.format(self.details)


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    comment = models.CharField(max_length=250)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20,blank=True)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment