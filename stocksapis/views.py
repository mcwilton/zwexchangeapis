
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import permissions
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import CompanySerializer
from .models import Company


from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')


@api_view(['GET'])
def api_overview(request):

    api_urls = {
        'List': '/company-list/',
    }

    return Response(api_urls)


# @api_view()
# def company_list(request):
#     companies = Company.objects.all()
#     serializer = CompanySerializer(companies, many=True)
#     return Response(serializer.data)


# @api_view()
# def company_detail(request, id):
#     company = get_object_or_404(Company, pk=id)
#     serializer = ProductSerializers(company)
#     return Response(serializer.data)


class CompanyList(APIView):
    """
    List all companies
    """
    def get(self, request, format=None):
        companies = Company.objects.all().order_by('id')
        serializer = CompanySerializer(companies, many=True)    
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)  
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    