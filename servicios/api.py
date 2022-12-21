from .models import Servicio, Payment_user, Expired_payments
from rest_framework import viewsets, filters
from .serializers import ServicioSerializer, PaymentSerializer, ExpiredSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.urls import reverse

class ServicioViewSet(viewsets.ReadOnlyModelViewSet): #Solo para list y retrieve
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['name']
    ordering = ('-id')



class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment_user.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['ExpirationDate','paymentDate']
    ordering = ('-id')



    def create(self, request, *args, **kwargs):

        creando=super().create(request, *args, **kwargs)  #Creo en la bbdd

        last = Payment_user.objects.order_by('-id').first()
        payment_user=Payment_user.objects.get(id=last.id)

        if payment_user.ExpirationDate < payment_user.paymentDate:
            expired_payment = Expired_payments(pay_user_id=payment_user, penalty_fee_amount=100)
            expired_payment.save()

        # llamo al método create del ModelViewSet
        # para crear el pago usando la información proporcionada
        return creando
        



class ExpiredViewSet(viewsets.ModelViewSet): #Solo GET Y POST
    queryset = Expired_payments.objects.all()
    serializer_class = ExpiredSerializer
    http_method_names = ['get', 'post']
 




from django.db import connection
class Todo(APIView):
    name = 'BIENVENIDO!  Puedes acceder a la V1 y V2 de app servicios'
    
    def get(self, request):

        principal="proyecto-unidad-5-production.up.railway.app"
        url_v1 = '/v1/'
        url_v2 = '/v2/'

        url_completa_v1=f"http://{principal}/login/versionamiento{url_v1}"
        url_completa_v2=f"http://{principal}/login/versionamiento{url_v2}"

        return Response({
            "Version 1": url_completa_v1,
            "Version 2": url_completa_v2,
        })
