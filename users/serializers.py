from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)
    is_superuser = serializers.BooleanField(default=False)  #agregado último
    is_staff = serializers.BooleanField(default=True)  #agregado último

    class Meta:
        model = User
        fields = ["email", "username", "password", 'is_superuser','is_staff']  #agregado último
  
    def validate(self, attrs):

        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("El email ya ha sido usado")
        return super().validate(attrs)

    def create(self, validated_data):               #Si no hago esto entonces la contraseña tal como está, porque el método create por defecto solo guarda la info pero no lo convierte a hash
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)

        return user

class GetUserSerializer(serializers.ModelSerializer):
    
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)   #Write_only es para que password no me aparezca en la salida de la api 

    class Meta:
        model = User
        fields = ["email", "username", "password","is_superuser" ]


class prueba_serializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)   #Write_only es para que password no me aparezca en la salida de la api 

    class Meta:
        model = User
        fields = ["email", "password"]
        