from django.db import models
from uuid import uuid4
import uuid
class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']  # Correct indentation
# Create your models here.
class  Product(models.Model):
    title = models.CharField(max_length=255) 
    description= models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    inventoey =models.IntegerField()
    last_update=models.DateField(auto_now=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']  # Correct indentation
   
    


class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'BRONZE'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    membership=models.CharField(  max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)
    

class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    customer = models.ForeignKey('Customer', on_delete=models.PROTECT)
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING,
    )
class OrderItem(models.Model):
    Order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6 , decimal_places=2)

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at =models.DateField(auto_now_add=True)

class CartItem(models.Model):
    cart =models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qunantity =models.PositiveSmallIntegerField()

class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='reviews')
    name=models.CharField(max_length=255)
    description =models.TextField()
    date=models.DateField(auto_now_add=True)



