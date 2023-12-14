from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *

# Create your views here.

@api_view(['GET'])
def index(request):
     return Response({'api is ok'})




@api_view(['GET'])
def Students(request):
     studentdetails=Studentdeatils.objects.all()
     serializer=Studentserializer(studentdetails,many=True)
     return Response(serializer.data)

@api_view(['GET'])
def Details(request,pk):
     try:
          studentdeatils=Studentdeatils.objects.get(id=pk)
     except:
          return Response({'student not available'})
     Serializer=Studentserializer(studentdeatils)
     return Response(Serializer.data)

@api_view(['POST'])
def addStudents(request):
     if request.method == 'POST':
          data=request.data
          serilalizer=Studentserializer(data=data)
          if serilalizer.is_valid():
               serilalizer.save()
               return Response(serilalizer.data)
          return Response(serilalizer.errors)
     

@api_view(['PUT','DELETE','PATCH'])
def updateStudents(request,pk):
     studentsdetails=Studentdeatils.objects.get(id=pk)
     data=request.data
     if request.method == 'PUT':
          serializer=Studentserializer(studentsdetails,data=data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors)
     if request.method == 'PATCH':
          serializer=Studentserializer(studentsdetails,data=data,partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors)
     if request.method == 'DELETE':
          studentsdetails.delete()
          return Response({'deleted sucessfully'})


     
     



