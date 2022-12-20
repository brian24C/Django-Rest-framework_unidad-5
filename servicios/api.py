from .models import Servicio, Payment_user, Expired_payments
from rest_framework import viewsets, filters
from .serializers import ServicioSerializer, PaymentSerializer, ExpiredSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

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
 

class ExpiredView(APIView):
    
    def get(self, request):
        expired = Expired_payments.objects.all()
        serializer = ExpiredSerializer(expired, many=True)
        return Response({
            "ok": True,
            "data": serializer.data
        })

    def post(self, request):
        serializer = ExpiredSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "ok": True,
                "message": "Expired created"
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok": False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)