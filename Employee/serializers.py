import uuid

from rest_framework import serializers
from Clients.models import Client
from Employees.models import EmployeeType
from Companies.models import Company
from Employee.models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'company', 'salary', 'employeeType', 'client')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'salary', 'employeeType', 'client')

    def create(self, data):
        company_id = data['company_id']
        employeeType = data['employeeType']
        client = data['client']

        company = Company.objects.get(pk=company_id)

        if not company:
            return {'success': 'false'}

        empId = 'emp-' + str(uuid.uuid4());
        Employee.objects.create(id=empId, name=data['name'], salary=data['salary'], client=client,
                                employeeType=employeeType, company=company)
        return {'success': 'true', 'emp-id': empId}

    def update(self, data, company_id, employee_id):
        employeeType = EmployeeType.objects.get(pk=data['employeeType']);
        client = Client.objects.get(pk=data['client']);
        company = Company.objects.get(pk=company_id)


        Employee.objects.filter(id=employee_id).delete()
        Employee.objects.create(id=employee_id, name=data['name'], salary=data['salary'], client=client,
                                employeeType=employeeType, company=company)
        return {'success': 'true'}