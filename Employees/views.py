from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer
from Companies.models import getCompanyIdFrom

class EmployeeDetails(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        company_id = getCompanyIdFrom(request)
        employeeType = EmployeeSerializer(data=request.data)
        if employeeType.is_valid():
            data = employeeType.save(company_id=company_id)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
