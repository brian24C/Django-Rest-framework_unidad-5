from servicios.models import Servicio, Payment_user, Expired_payments, PerfilDeUsuario
from rest_framework import viewsets, filters
from .serializers import ServicioSerializer, PaymentSerializer, ExpiredSerializer, PerfilSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated



class ServicioViewSet(viewsets.ModelViewSet): 
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['name']
    #ordering = ('-id')
    #http_method_names = ['get']
    permission_classes=[IsAuthenticated]
    throttle_scope = 'servicio'




        

class PaymentViewSet( viewsets.ModelViewSet):

    queryset = Payment_user.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['ExpirationDate','paymentDate']
    #ordering = ('-id')
    permission_classes=[IsAuthenticated]


    
    throttle_scope = 'pagos'

    def create(self, request, *args, **kwargs):
        # llamo al método create del ModelViewSet

        payment_data = request.data
        #print(payment_data["csrfmiddlewaretoken"]) si pongo esto me sale error 
        print(request.user)

        creando=super().create(request, *args, **kwargs)  #Creo en la bbdd

        
        last = Payment_user.objects.order_by('-id').first()
        payment_user=Payment_user.objects.get(id=last.id)

        if payment_user.ExpirationDate < payment_user.paymentDate:
            expired_payment = Expired_payments(pay_user_id=payment_user, penalty_fee_amount=100)
            expired_payment.save()

      
        return creando
        

class ExpiredViewSet(viewsets.ModelViewSet): #Solo GET Y POST
    queryset = Expired_payments.objects.all()
    serializer_class = ExpiredSerializer
    http_method_names = ['get', 'post']
    permission_classes=[IsAuthenticated]
    #ordering = ('-id')
    throttle_scope = 'expired'


class PerfilViewset(viewsets.ModelViewSet):
    queryset = PerfilDeUsuario.objects.all()
    serializer_class = PerfilSerializer
    