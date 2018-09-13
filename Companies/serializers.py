import uuid

from rest_framework import serializers
from Companies.models import Company

class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
