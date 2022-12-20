from streamingPagos.models import Pagos
from rest_framework import viewsets
from .serializers import PagoSerializer
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 

class PagoViewSet(viewsets.ModelViewSet):

    queryset = Pagos.objects.get_queryset().order_by('id')
    serializer_class = PagoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]


    search_fields = ['usuario', 'fecha_pago', 'servicio']
    throttle_scope = 'pagos'

    http_method_names = ['get', 'post']