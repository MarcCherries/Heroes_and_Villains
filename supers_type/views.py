from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import SuperType
from .serializer import SuperTypeSerializer



# Create your views here.
@api_view(['GET'])
def supertype_list(request):
    supertype = SuperType.objects.all()
    serializer = SuperTypeSerializer(supertype, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

