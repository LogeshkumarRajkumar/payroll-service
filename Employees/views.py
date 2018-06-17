from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import EmployeeSerializer
import jwt

class EmployeeDetails(APIView):
    permission_classes = [AllowAny]
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, company_id):
        print("hello")
        return Response({"companyId:": company_id}, status=status.HTTP_200_OK)

    def post(self, request, company_id, format=None):
        authtoken = request.META['HTTP_AUTHORIZATION'].split()
        answer = jwt.decode(authtoken[1], verify=False)
        print answer['user_id']
        employeeType = EmployeeSerializer(data=request.data)
        if employeeType.is_valid():
            data = employeeType.save(company_id=company_id)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)
