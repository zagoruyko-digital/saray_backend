from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from .serializers import *

@csrf_exempt
def user(request):
   current_user = User.objects.get(id=1)
   
   UserViewSet.get_serializer_class

@permission_classes((AllowAny,))
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = News.objects.all()

   def get_serializer_class(self):
        if self.action == 'list':
           return NewsDetailSerializer
        return NewsDetailSerializer

@permission_classes((AllowAny,))
class CategoryqViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = Categoryq.objects.all()

   def get_serializer_class(self):
        if self.action == 'list':
           return CategoryqSerializer
        return CategoryqSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
   serializer_class = ManagerInfoSerializer

   def get_queryset(self):
      return User.objects.filter(id=self.request.user.id)