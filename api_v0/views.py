from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from .serializers import *

@permission_classes((AllowAny,))
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
   queryset = News.objects.all()

   def get_serializer_class(self):
        if self.action == 'list':
           return NewsDetailSerializer
        return NewsDetailSerializer