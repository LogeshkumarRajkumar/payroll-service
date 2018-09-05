from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Clients.serializers import ClientSerializer
from Companies.models import getCompanyIdFrom


class ClientDetails(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        companyid = getCompanyIdFrom(request)
        client = ClientSerializer(data=request.data)
        print(client)
        if client.is_valid():
            data = client.save(company_id=companyid)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
