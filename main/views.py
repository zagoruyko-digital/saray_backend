from django.contrib.auth import authenticate
from django.core import serializers
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username').lower()
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if not user:
        new_user = User.objects.create(username=username)
        new_user.set_password(password)
        new_user.save()

        group = Group.objects.get(name='Customer')
        group.user_set.add(new_user)

        user = authenticate(username=username, password=password)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)