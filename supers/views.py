import imp
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import supers_type
from supers_type.models import SuperType
from .serializer import CharacterSerializer
from .models import Character
from rest_framework import status
from django.shortcuts import get_object_or_404





# Create your views here.
@api_view(['GET', 'POST'])
def character_list(request):
    type_param = request.query_params.get('type')
    sort_param = request.query_params.get('sort')
    characters = Character.objects.all()
        
    if  request.method == 'GET':
        if type_param:
            characters = characters.filter(super_type__super_type=type_param)

        if sort_param:
            characters = characters.order_by(sort_param)
        
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data)

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


@api_view(['GET'])
def supertypes_list(request):
    supertypes = SuperType.objects.all()
    
    custom_response_dict = {}
    for type in supertypes:
        characters = Character.objects.filter(super_type_id=type.id)
        character_serializer = CharacterSerializer(characters, many=True)
        custom_response_dict[type.super_type] = {
            "super_type": type.super_type,
            "character" : character_serializer.data

            
        }
    return Response(custom_response_dict)