
from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import generics ,status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer, GetUserSerializer
from .tokens import create_jwt_pair_for_user
from .models import User


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import login
from django.urls import reverse

from django.shortcuts import redirect

from rest_framework import viewsets
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request:Request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
               #Me ejecuta el metodo create del serializers 
           
            if data.get("is_superuser") is not None:
                    serializer.is_superuser = True
            if data.get("is_staff") is not None:
                    serializer.is_staff = True
         
            user = serializer.save()
        

            return Response({"message": "el usuario se creó correctamente" , "data": serializer.data},  status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)

    def get(self, request:Request):
        content={"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


class LoginView(APIView):

    def post(self, request:Request):
        email=request.data.get('email')
        password=request.data.get('password')
      
        user = authenticate(request, email=email, password=password)

        if user is not None:
            #usuario=User.objects.filter(email=email)[0]    También funciona si pongo este
            usuario=User.objects.get(email=email)
            tokens = create_jwt_pair_for_user(user)
           
         
            data_user={
                "email": usuario.email,
                "username": usuario.username,
                "is_superuser": usuario.is_superuser,
                "id": usuario.id,
            }
      


            response = {
                "message": "Logeado Exitoso",
                "data": data_user,
                "tokens": tokens,
            }     

        
            print(data_user)
            return Response(data=response, status=status.HTTP_200_OK)      
            
        else:
            return Response(data={"message": "correo inválido o contraseña incorrecta"})

    def get(self, request:Request):

        content={"user": str(request.user), "auth": str(request.auth) , "formato para el campo Content" : {"email": "castro@hotmail.com", "password": "brianjosue"}}
        return Response(data=content, status=status.HTTP_200_OK)

        
class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()




class Todo(APIView):
    name = 'Signup or Login para acceder'

    def get(self, request):
        throttle_classes=[UserRateThrottle]
        principal="proyecto-unidad-5-production.up.railway.app"
        url_signup = reverse('signup')
        url_login = reverse('login')
        print(request.user)
        url_crear=f"http://{principal}{url_signup}"
        url_entrar=f"http://{principal}{url_login}"
        
        return Response({

            "CREAR CUENTA": url_crear,
            "LOGEARTE": url_entrar,
        })

   

class MyView(APIView):
    def post(self, request, *args, **kwargs):
        browser_url = request.data['browser_url']
        # Ahora puedes usar la variable browser_url para obtener la URL del navegador