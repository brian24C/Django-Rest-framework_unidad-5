from rest_framework import routers
from .api import ServicioViewSet, PaymentViewSet, ExpiredView,ExpiredViewSet
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

router.register(r'pagoStreaming', PagoViewSet, basename='pagos')

urlpatterns = [
    #path("expired2/", ExpiredView.as_view(), name="expired_"),
    #path("expired/", ExpiredViewSet.as_view(), name="expired2"),
    #re_path(r'^expired/', ExpiredViewSet.as_view(), name="expired2"),
    #path('general/', include((router.urls))),

]

urlpatterns += router.urls