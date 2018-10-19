from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from Employee.serializers import EmployeeSerializer, EmployeeListSerializer
from Companies.models import getCompanyIdFrom
from Clients.models import Client
from Employees.models import EmployeeType
from Employee.models import Employee


class EmployeeDetails(viewsets.ModelViewSet):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, employee_id):
        employee = Employee.objects.filter(id=employee_id)
        if employee[0].company_id != getCompanyIdFrom(request):
            return Response({"Success": "false", "error": "Invalid employee"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = EmployeeListSerializer(employee, many=True)
        return Response(serializer.data[0], status=status.HTTP_200_OK)

    def list(self, request):
        companyid = getCompanyIdFrom(request)
        queryset = Employee.objects.filter(company=companyid)
        serializer = EmployeeListSerializer(queryset, many=True)
        return Response({"Success": "true", "response": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        companyId = getCompanyIdFrom(request)
        employee = EmployeeSerializer(data=request.data)
        print(employee)
        if employee.is_valid():
            data = employee.save(company_id=companyId)
            return Response({"Success": "true", "response": data}, status=status.HTTP_201_CREATED)
        return Response({"Success": "false", "errorMessage": "Field validation errors", "error": employee.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, employee_id, format=None):
        companyId = getCompanyIdFrom(request)
        employee = Employee.objects.filter(id=employee_id).first()
        if employee.company_id != getCompanyIdFrom(request):
            return Response({"Success": "false", "error": "Invalid Employee Type"}, status=status.HTTP_401_UNAUTHORIZED)

        serializedData = EmployeeSerializer(data=request.data)
        if serializedData.is_valid():
            data = serializedData.update(data=request.data, company_id=companyId, employee_id=employee_id)
            return Response({"Success": "true", "response": data}, status=status.HTTP_201_CREATED)
        return Response({"Success": "false", "errorMessage": "Field validation errors", "error": employee.errors}, status=status.HTTP_400_BAD_REQUEST)

