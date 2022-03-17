import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import CharacterSerializer
from .models import Character
from rest_framework import status
from django.shortcuts import get_object_or_404





# Create your views here.
@api_view(['GET', 'POST'])
def character_list(request):
    if request.method == 'GET':
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CharacterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def character_detail(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method == 'GET':
       serializer = CharacterSerializer(character)
       return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CharacterSerializer(character, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        character.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


