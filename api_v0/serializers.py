from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Manager, News, Categoryq

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

class NewsDetailSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer()

    class Meta:
        model = News
        fields = [
            'manager',
            'id',
            'title',
            'body',
            'cover'
        ]

class CategoryqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoryq
        fields = [
            'id',
            'category_name',
            'title',
            'description',
            'cover'
        ]