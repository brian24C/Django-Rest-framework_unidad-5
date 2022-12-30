from datetime import datetime
from django.db import models
from users.models import User

# Create your models here.
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%dT%H:%M")


class Servicio(models.Model):
    name=models.CharField(max_length=500)
    descripcion=models.CharField(max_length=500)
    Logo=models.ImageField(upload_to="images")

    class Meta:
        db_table = 'servicios'

    def __str__(self) -> str:
        return f"Servicio: {self.name}"


class Payment_user(models.Model):

    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id_payment")
    service = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name="service_id_payment")
    amount = models.IntegerField()
    paymentDate=models.DateTimeField(auto_now_add=True)
    ExpirationDate=models.DateTimeField()

    def __str__(self) -> str:
        return f"payment_User: {self.user.username}"

    class Meta:
        db_table = 'payment_user'

class Expired_payments(models.Model):
    pay_user_id=models.ForeignKey(Payment_user, on_delete=models.CASCADE, related_name="pay_id_Expired")
    penalty_fee_amount=models.IntegerField(default=100)

    class Meta:
        db_table = 'expired_payments'

    def __str__(self) -> str:
        return f"Expired User: {self.pay_user_id.id}"


class PerfilDeUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    perfil=models.ImageField(upload_to="FotoPerfil")
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id_perfil")

    class Meta:
        db_table = 'PerfilDeUsuario'