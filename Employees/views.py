from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import EmployeeSerializer, EmployeeListSerializer, WageListSerializer
from Companies.models import getCompanyIdFrom
from .models import EmployeeType, EmployeeTypeDetails


class WageDetails(viewsets.ModelViewSet):
    def list(self, request, employee_typeid):
        employeeType = EmployeeType.objects.filter(id=employee_typeid)
        employeeTypeDetails = EmployeeTypeDetails.objects.filter(employeeType=employee_typeid)
        if employeeType[0].company_id != getCompanyIdFrom(request):
            return Response({"Success": "false", "error": "Invalid Employee Type"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = WageListSerializer(employeeTypeDetails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EmployeeDetails(viewsets.ModelViewSet):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, employee_typeid):
        queryset = EmployeeType.objects.filter(id=employee_typeid)
        if queryset[0].company_id != getCompanyIdFrom(request):
            return Response({"Success": "false", "error": "Invalid Employee Type"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = EmployeeListSerializer(queryset, many=True)
        return Response(serializer.data[0], status=status.HTTP_200_OK)

    def list(self, request):
        companyid = getCompanyIdFrom(request)
        queryset = EmployeeType.objects.filter(company=companyid)
        serializer = EmployeeListSerializer(queryset, many=True)
        return Response({"Success": "true", "response": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        company_id = getCompanyIdFrom(request)
        employeeType = EmployeeSerializer(data=request.data)
        if employeeType.is_valid():
            data = employeeType.save(company_id=company_id)
            return Response({"Success": "true", "response": data}, status=status.HTTP_201_CREATED)
        return Response({"Success": "false", "errorMessage": "Field validation errors", "error": employeeType.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, employee_typeid, format=None):
        company_id = getCompanyIdFrom(request)
        employee = EmployeeType.objects.filter(id=employee_typeid).first()
        if employee.company_id != getCompanyIdFrom(request):
            return Response({"Success": "false", "error": "Invalid Employee Type"}, status=status.HTTP_401_UNAUTHORIZED)

        serializedData = EmployeeSerializer(data=request.data)
        if serializedData.is_valid():
            data = serializedData.update(data=request.data, company_id=company_id, employeetype_id=employee_typeid)
            return Response({"Success": "true", "response": "updated"}, status=status.HTTP_201_CREATED)
        return Response({"Success": "false", "errorMessage": "Field validation errors", "error": serializedData.errors},
                        status=status.HTTP_400_BAD_REQUEST)
