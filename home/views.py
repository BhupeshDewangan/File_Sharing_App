# from tkinter import E
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from rest_framework.parsers import MultiPartParser


def home(request):
    return render(request ,'home.html')
    # return render(request ,'try.html')


def download(request , uid):
    return render(request , 'download.html' , context = {'uid' : uid})


# whenever the file will upload, it will show the success and failure msg in console of web browsers

# APIView class provided by Django REST framework. It is used to handle file uploads in a Django application.

class HandleFileUpload(APIView):
    parser_classes = [MultiPartParser]
    def post(self , request):
        try:
            data = request.data

            serializer = FileListSerializer(data = data)
        
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status' : 200,
                    'message' : 'files uploaded successfully',
                    'data' : serializer.data
                })
            
            return Response({
                'status' : 400,
                'message' : 'somethign went wrong',
                'data'  : serializer.errors
            })
        except Exception as e:
            print(e)
