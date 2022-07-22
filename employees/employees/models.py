from django.db import models


# Model class for team members details
class Employees(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phone = models.IntegerField
    role = models.CharField(max_length=10)
