from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'categoryq', CategoryqViewSet)
router.register(r'user', UserViewSet, base_name='CurrentUser')


urlpatterns = router.urls