from django.db import models
from django.contrib.postgres.fields import ArrayField

# ABODJI Kondi Kalèd


# Category
class Category(models.Model):
    title = models.CharField(max_length=100)
    urls = ArrayField(models.URLField(max_length=200), size=3)

    def __str__(self):
        return "{}".format(self.title)


# Cars table of the database
class Car(models.Model):
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=50, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)
    urls = ArrayField(models.URLField(max_length=200), size=3)

    def __str__(self):  # For the desplay in the db
        return "{}_{}".format(self.brand, self.model)


"""
Name :ABODJI Kondi Kalèd
"""


# customer
class Customer(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=50, null=False)
    address = models.CharField(max_length=350)
    cni = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Booking
class Booking(models.Model):
    date = models.DateField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    # Linking management
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}_{}".format(self.customer.name, self.car.brand, self.car.model)


# Car rating
class Rating(models.Model):
    rate = models.FloatField(null=False)
    rated_car = models.ForeignKey(Car, on_delete=models.CASCADE)

    # user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)


# Comment
class Comment(models.Model):
    comment = models.TextField(max_length=500)
    commented_car = models.ForeignKey(Car, on_delete=models.CASCADE)

    # user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
