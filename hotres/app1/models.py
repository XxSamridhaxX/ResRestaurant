from django.db import models
from django.contrib.auth.models import User

# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to the built-in User model
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
# TODO: since user already contains first name, last name, phone number and email we only have to add a phone number to it.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Links to the built-in User model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number} - Capacity {self.capacity}"

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Many-to-One relationship
    table = models.ForeignKey(Table, on_delete=models.CASCADE)  # Many-to-One relationship
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.customer} on {self.reservation_date} at {self.reservation_time}"
