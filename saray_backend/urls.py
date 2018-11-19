from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from main.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('login/', login),
    url(r'^api/v0/', include('api_v0.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)