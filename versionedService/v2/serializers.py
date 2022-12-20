
from datetime import datetime
from rest_framework import serializers
from servicios.models import Servicio, Payment_user, Expired_payments


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Servicio
        fields = '__all__' #para todos los campos.


    def validate_title(self,value):
        if "$" in value:
            raise serializers.ValidationError("Error, $ encontrado")
        return value

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment_user
        fields = '__all__' #para todos los campos.


class ExpiredSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expired_payments
        fields = '__all__' #para todos los campos.


#---------------------------------------



