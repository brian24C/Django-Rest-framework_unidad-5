from rest_framework import routers
from .api import ServicioViewSet, PaymentViewSet,ExpiredViewSet
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from streamingPagos.api import PagoViewSet


router = routers.DefaultRouter()
router.register('readService', ServicioViewSet, basename="service")
router.register('payment', PaymentViewSet, basename="PaymentViewSet")
router.register('expired', ExpiredViewSet, basename="ExpiredViewSet")


urlpatterns = [
    
]

urlpatterns += router.urls