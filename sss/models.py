from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    postcode = models.SmallIntegerField()

class Customer(models.Model):
    name = models.CharField(max_length=100)

class BillingAddress(Address):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shippingaddress = models.OneToOneField(Address, on_delete=models.CASCADE)

class OrderPayment(models.Model):
    cardNumber = models.BigIntegerField()
    txnId = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    billingaddress = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)

class OrderItem(models.Model):
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

