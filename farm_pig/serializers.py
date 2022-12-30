
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Pig ,Birth

class PigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pig
        fields = '__all__'

class BirthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Birth
        fields = '__all__'