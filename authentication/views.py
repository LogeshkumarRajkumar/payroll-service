import sys
sys.path.append('..')
from .serializers import CompanySerializer
from .models import Company
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class CompanyDetail(APIView):
    permission_classes = [AllowAny]
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        company = CompanySerializer(data=request.data)
        if company.is_valid():
            data = company.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(company.errors, status=status.HTTP_400_BAD_REQUEST)
