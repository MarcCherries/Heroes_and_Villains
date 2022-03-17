import imp
from .models import SuperType
from rest_framework import serializers


class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['id', 'super_type']
