from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save,m2m_changed
class Collection(models.Model):
    p_name=models.CharField(max_length=100)
    def __str__(self):
        return self.p_name

class Product(models.Model):
    collect=models.ForeignKey(Collection,on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    brand=models.CharField(max_length=50)
    features=models.CharField(max_length=100)
    img=models.FileField(upload_to='media')
    stock=models.IntegerField()

    def __str__(self):
        return self.name+self.brand


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    name=models.CharField(max_length=50)
    mob=models.IntegerField()
    pin=models.IntegerField()
    address = models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Cart(models.Model):
    cust=models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    products=models.ManyToManyField(Product)
    total=models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    def _str__(self):
        return str(self.pk)

def m2mchanged_product(sender,action,instance,*args,**kwargs):
    products=instance.products.all()
    total=0
    for product in products:
        total+=product.price
    instance.total=total
    instance.save()
m2m_changed.connect(m2mchanged_product,sender=Cart.products.through)

class Order(models.Model):
    cust=models.ForeignKey(Customer,on_delete=models.CASCADE)
    products=models.ManyToManyField(Product,blank=True,null=True)
    cash=models.DecimalField(max_digits=100,decimal_places=2,default=0.00)
    def __str__(self):
        return str(self.pk)

def cash_changed(sender,action,instance,*args,**kwrgs):
    products=instance.products.all()
    cash=0
    for p in products:
        cash+=p.price
    instance.cash=cash
    instance.save()

m2m_changed.connect(cash_changed,sender=Order.products.through)