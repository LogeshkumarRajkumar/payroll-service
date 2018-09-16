from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Companies.models import getCompanyIdFrom, Company
from rest_framework.permissions import AllowAny
from .serializers import CompanyListSerializer

class CompanyDetail(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        company_id = getCompanyIdFrom(request)
        company = Company.objects.filter(id=company_id)
        serializer = CompanyListSerializer(company, many=True)
        return Response({"Success": "true", "response": serializer.data[0]}, status=status.HTTP_200_OK)
