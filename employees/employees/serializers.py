from rest_framework import serializers
from .models import Employees


# Class to serialize model data returned
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
