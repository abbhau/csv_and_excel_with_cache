from django.shortcuts import render
from .serializers import Student, StudentSrializer
from rest_framework.views import APIView
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .pagination import LargeResultsSetPagination
from drf_yasg import openapi
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.generics import ListAPIView

# Create your views here.

class StudentList(ListAPIView):
    #pagination_class = LimitOffsetPagination     
    queryset = Student.objects.all()
    serializer_class = StudentSrializer

class StudentView(APIView):                                                 
    def get(self, request ):
        obj = Student.objects.all()
        serializer = StudentSrializer(obj, many=True)
        mv = cache.get("data")
        if mv:
           return Response({"data":mv}, status=status.HTTP_200_OK)
        
        data = serializer.data
        cache.set("data",data, 240)
        return Response({"data":data}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=StudentSrializer)
    def post(self, request):
        serializer = StudentSrializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

