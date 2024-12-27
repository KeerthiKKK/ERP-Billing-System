from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    business_title = models.CharField(max_length=100, blank=True, null=True)
    business_address = models.TextField(max_length=400, blank=True, null=True)
    business_email = models.EmailField(blank=True, null=True)
    business_phone = models.CharField(max_length=20, blank=True, null=True)
    business_gst = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    
class Billing(models.Model):
    bill_id = models.PositiveIntegerField()
    bill_items=models.CharField(max_length=255)
    bill_address=models.CharField(max_length=255)
    bill_amount=models.FloatField()
    bill_date=models.DateField()

    def __str__(self):
        return f"BILL.NO:{self.bill_id}"
    
class Products(models.Model):
    product_id=models.PositiveIntegerField()
    product_category=models.CharField(max_length=255)
    product_name=models.CharField(max_length=255)
    product_quantity=models.IntegerField()
    product_price=models.FloatField()
    
    def __str__(self):
        return f"Product_Name:{self.product_name}"
    
class Stock(models.Model):
    Product_Stock_id=models.IntegerField()
    Stock_number = models.IntegerField(default=0)

    def __str__(self):
        return f"Stock_ID:{self.Product_Stock_id}"
    


    



