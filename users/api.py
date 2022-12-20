
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
        print(email)
        print(password)
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:

            id_usuario=User.objects.filter(email=email).values('id')[:1]

            #usuario=User.objects.filter(email=email)[0]    También funciona si pongo este
            usuario=User.objects.get(email=email)
            print(usuario)
            tokens = create_jwt_pair_for_user(user)
            if tokens: 
                
                login(self.request, user)
            resp={
                    "message": "LOGEADO CORRECTAMENTE", 
                    "email": email, 
                    "tokens":tokens, 
                    }
            
            #return Response(data=resp, status=status.HTTP_200_OK)
            #return HttpResponseRedirect(reverse('PaymentViewSet', kwargs={'app_name': 'servicios'}))
            #return redirect(PaymentViewSet.as_view({'get': 'list', 'post': 'create'}))

            return redirect('tienda/')       #FUNCIONA

        else:
            return Response(data={"message": "correo inválido o contraseña incorrecta"})

    def get(self, request:Request):

        content={"user": str(request.user), "auth": str(request.auth) , "formato para el campo Content" : {"email": "brian2@hotmail.com", "password": "1234"}}


        return Response(data=content, status=status.HTTP_200_OK)

        
class GetUsers(viewsets.ReadOnlyModelViewSet):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()



from django.contrib.sites.shortcuts import get_current_site

class Todo(APIView):
    name = 'Signup or Login para ingresar a la Tienda'

    def get(self, request):
        throttle_classes=[UserRateThrottle]
        principal="proyecto-unidad-5-production.up.railway.app"
        url_signup = reverse('signup')
        url_login = reverse('login')

        url_crear=f"http://{principal}{url_signup}"
        url_entrar=f"http://{principal}{url_login}"
        print(my_view(request))
        return Response({

            "CREAR CUENTA": url_crear,
            "LOGEARTE": url_entrar,
        })

   



def my_view(request):
    # Obtener el objeto Site actual
    site = get_current_site(request)
    # Obtener la dirección del sitio
    site_address = site.domain
    print(site_address)
    # Usar la dirección del sitio para construir la URL completa de la vista
    full_url = f"http://{site_address}"


class MyView(APIView):
    def post(self, request, *args, **kwargs):
        browser_url = request.data['browser_url']
        # Ahora puedes usar la variable browser_url para obtener la URL del navegador