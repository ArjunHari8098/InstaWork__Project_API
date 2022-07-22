# To access superclass privilages
from django.contrib import admin
from .models import Employees

admin.site.register(Employees)
