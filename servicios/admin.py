from django.contrib import admin
from .models import Servicio, Payment_user, Expired_payments
# Register your models here.

admin.site.register(Servicio)
admin.site.register(Payment_user)
admin.site.register(Expired_payments)