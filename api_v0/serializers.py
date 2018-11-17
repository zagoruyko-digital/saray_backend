from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Manager

class ManagerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
        ]

class ManagerSerializer(serializers.ModelSerializer):
    user = ManagerInfoSerializer()

    class Meta:
        model = Manager
        fields = [
            'user',
            'image'
        ]