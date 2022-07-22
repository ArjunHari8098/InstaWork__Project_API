from django.http import JsonResponse
from .models import Employees
from .serializers import EmployeesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Method to expose get and post methods
# Functionalities of fetch and insert team member details to db
@api_view(['GET', 'POST'])
def get_employees(request, format=None):
    if request.method == 'GET':
        team = Employees.objects.all()
        employeeSerial = EmployeesSerializer(team, many=True)
        return JsonResponse({'team': employeeSerial.data}, safe=False)
    if request.method == 'POST':
        eSerial = EmployeesSerializer(data=request.data)
        if eSerial.is_valid():
            eSerial.save()
            return Response(eSerial.data, status=status.HTTP_200_OK)


# Method to expose PUT and DELETE methods
# Functionalities of update and delete team members
@api_view(['GET', 'PUT', 'DELETE'])
def update_delete_employee(request, id, format=None):
    try:
        emp = Employees.objects.get(pk=id)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        employeeSerial = EmployeesSerializer(emp)
        return JsonResponse(employeeSerial.data)
    if request.method == 'PUT':
        eSerial = EmployeesSerializer(emp, data=request.data)
        if eSerial.is_valid():
            eSerial.save()
            return Response(eSerial.data, status=status.HTTP_200_OK)
        return Response(eSerial.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
