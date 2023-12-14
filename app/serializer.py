from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from rest_framework.response import Response



class Studentserializer(ModelSerializer):
    class Meta:
        model=Studentdeatils
        fields='__all__'


    def validate(self, attrs):
        if int(attrs['age'])  < 18 :
            raise serializers.ValidationError('age should be greater than 18')
    
        if len(attrs['name']) < 5:
            raise serializers.ValidationError("name should be greater than 5 letters")

        return attrs