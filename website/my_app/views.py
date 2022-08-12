from time import time
from urllib import response
from django.shortcuts import render, redirect
from my_app.models import Student
from .serializers import StudentSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date =  request.POST.get('date')
        student = Student (
            name = name,
            description = description,
            date = date,

        )
        student.save()
    return render(request, 'index.html')

def home(request):
    response = Student.objects.all()
    return render(request,'home.html',{'response':response})


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'update':'/taskupdate/<str:pk>/',
        'delete':'/taskdelete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def student_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many= True) #python data

    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request,pk):
    task = Student.objects.get(id = pk)
    serializer = StudentSerializer(instance=task, data=request.data) #python data

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    task = Student.objects.get(id = pk)
    task.delete()
    return Response('Item succsesfully deleted')



