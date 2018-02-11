#from ..company.models import Company
from rest_framework import serializers
from .models import User, Company
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

class CompanySerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Company
        fields = ('name', 'creator')

    def create(self, data):
        user_data = data.pop('creator')
        user = User.objects.create_superuser(**user_data)
        print('creator', data)
        company = Company.objects.create(creator=user, **data)
        return company