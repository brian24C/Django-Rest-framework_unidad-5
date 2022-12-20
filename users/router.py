
from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import api


router = routers.DefaultRouter()

router.register("get", api.GetUsers)



urlpatterns=[
    path("signup/", api.SignUpView.as_view(), name="signup"),
    path("login/", api.LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/regresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", api.Todo.as_view(), name="todo"),

]

urlpatterns += router.urls