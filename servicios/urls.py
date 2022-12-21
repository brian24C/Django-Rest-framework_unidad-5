from rest_framework import routers
from .api import ServicioViewSet, PaymentViewSet,ExpiredViewSet, Todo
from django.urls import path, re_path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from streamingPagos.api import PagoViewSet
from versionedService.v1.router import urlpatterns as api_v1
from versionedService.v2.router import urlpatterns as api_v2


router = routers.DefaultRouter()




urlpatterns = [
    #path("expired2/", ExpiredView.as_view(), name="expired_"),
    #path("expired/", ExpiredViewSet.as_view(), name="expired2"),
    #re_path(r'^expired/', ExpiredViewSet.as_view(), name="expired2"),
    path('', Todo.as_view(), name="todo"),

    path('v1/', include((api_v1)), name="v1"),
    path('v2/', include((api_v2)), name="v2"),
    
]

urlpatterns += router.urls