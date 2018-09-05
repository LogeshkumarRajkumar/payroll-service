# from ..Companies.models import Companies
from rest_framework import serializers
from .models import User
from Companies.models import Company
import uuid


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')


class CompanySerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Company
        fields = ('name', 'creator')

    def create(self, data):
        user_data = data.pop('creator')
        user_id = 'user-' + str(uuid.uuid4());
        user = User.objects.create_superuser(id=user_id, **user_data)

        company_id = 'comp-' + str(uuid.uuid4());
        Company.objects.create(id=company_id, creator=user, **data)
        return {'success': 'true'}
