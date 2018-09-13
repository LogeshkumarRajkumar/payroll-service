from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from Clients.serializers import ClientSerializer, ClientListSerializer
from Companies.models import getCompanyIdFrom
from Clients.models import Client


class ClientDetails(viewsets.ModelViewSet):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, client_id):
        client = Client.objects.filter(id=client_id)
        if client[0].company_id != getCompanyIdFrom(request):
            return Response({"Success": "false"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ClientListSerializer(company, many=True)
        return Response(serializer.data[0], status=status.HTTP_200_OK)

    def list(self, request):
        companyid = getCompanyIdFrom(request)
        queryset = Client.objects.filter(company=companyid)
        serializer = ClientListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        companyid = getCompanyIdFrom(request)
        client = ClientSerializer(data=request.data)
        print(client)
        if client.is_valid():
            data = client.save(company_id=companyid)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, client_id, format=None):
        client = Client.objects.filter(id=client_id).first()
        if client.company_id != getCompanyIdFrom(request):
            return Response({"Success": "false"}, status=status.HTTP_401_UNAUTHORIZED)

        client = ClientSerializer(client, data=request.data)
        print(client)
        if client.is_valid():
            data = client.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

