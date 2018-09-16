from rest_framework import serializers
from .models import EmployeeType, EmployeeTypeDetails
from Companies.models import Company
from django.core.exceptions import ValidationError

import uuid


class WageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTypeDetails
        fields = ('startTime', 'endTime', 'wageMultiple')


class EmployeeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeType
        fields = ('id', 'name', 'salaried',)


class WageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTypeDetails
        fields = ('startTime', 'endTime', 'wageMultiple')


class EmployeeSerializer(serializers.ModelSerializer):
    wageDetails = WageSerializer(many=True)

    class Meta:
        model = EmployeeType
        fields = ('name', 'salaried', 'wageDetails')

    def validate_time(self, startTime, endTime):
        if endTime < startTime:
            return False
        return True

    def create(self, data):
        company_id = data['company_id']
        company = Company.objects.get(pk=company_id)
        if not company:
            return {'success': 'false'}

        wageDetails = data['wageDetails']
        if not 'salaried' in data:
            return {'message': 'Salaried flag is mandatory in request'}

        if data['salaried'] is True:
            EmployeeType.objects.create(name=data['name'], company=company, salaried=data['salaried'])

        if data['salaried'] is not True:
            for wageDetail in wageDetails:
                isvalid = self.validate_time(wageDetail['startTime'], wageDetail['endTime'])
                if not isvalid:
                    return {'success': 'false',
                            'error': 'Invalid Start Time and End Time'}

            employeeType = EmployeeType.objects.create(name=data['name'], company=company, salaried=data['salaried'])
            for wageDetail in wageDetails:
                EmployeeTypeDetails.objects.create(employeeType=employeeType, startTime=wageDetail['startTime'],
                                                   endTime=wageDetail['endTime'])
        return {'success': 'true'}
