from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character 
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catch_phrase', 'super_type']
