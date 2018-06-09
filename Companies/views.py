from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class CompanyDetail(APIView):
    permission_classes = [AllowAny]
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, company_id):
        return Response({"companyId:": company_id }, status=status.HTTP_200_OK)
