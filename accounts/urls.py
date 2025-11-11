from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, health_check

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/health/', health_check, name='health-check'),
]