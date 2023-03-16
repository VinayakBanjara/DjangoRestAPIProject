from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Company, Employee, ExternalUser
from api.serializers import CompanySerializer, EmployeeSerializer, UserSerializer


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    # companies/{companyId}/employees/
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)

            employees = Employee.objects.filter(company=company)
            employees_serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(employees_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'Message': 'company might not exist!! Error'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = ExternalUser.objects.all()
    serializer_class = UserSerializer
