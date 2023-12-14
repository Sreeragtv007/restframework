from django.urls import path
from .views import *

urlpatterns = [
    path('index',index),
    path('',Students),
    path('details/<str:pk>/',Details),
    path('addStudents',addStudents),
    path('update/<str:pk>/',updateStudents)


]
