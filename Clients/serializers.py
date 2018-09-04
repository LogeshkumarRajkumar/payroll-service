import uuid

from rest_framework import serializers
from Clients.models import Client
from Companies.models import Company


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('name',)

    def create(self, data):
        company_id = data['company_id']
        print('here')
        company = Company.objects.get(pk=company_id)
        if not company:
            return {'success': 'false'}

        clientId = 'client-' + str(uuid.uuid4());
        Client.objects.create(id=clientId, name=data['name'], company=company)
        return {'success': 'true', 'client-id': clientId}

