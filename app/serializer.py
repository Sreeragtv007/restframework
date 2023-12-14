from rest_framework.serializers import ModelSerializer
from .models import *


class Studentserializer(ModelSerializer):
    class Meta:
        model=Studentdeatils
        fields='__all__'