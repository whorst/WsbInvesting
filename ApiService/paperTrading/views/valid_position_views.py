# from  import Numberid, TickersTable
from rest_framework import generics
from common.models import Numberid
from common.serializers import PositionSerializer
#For Rest Based Views
# Create your views here.
# https://www.django-rest-framework.org/api-guide/views/

class ValidPosition(generics.ListAPIView):
    serializer_class = PositionSerializer
    lookup_url_kwarg = "ticker"

    def get_queryset(self):
        positions = Numberid.objects.filter(tickersymbol=self.kwargs['ticker'])
        return positions

class Puts(generics.ListAPIView):
    serializer_class = PositionSerializer
    lookup_url_kwarg = "ticker"

    def get_queryset(self):
        positions = Numberid.objects.filter(iscall=0)
        return positions

class Calls(generics.ListAPIView):
    serializer_class = PositionSerializer
    lookup_url_kwarg = "ticker"

    def get_queryset(self):
        positions = Numberid.objects.filter(iscall=1)
        return positions
