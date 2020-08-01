# from  import Numberid, TickersTable
from rest_framework import generics
from ApiService.common.models import Numberid
from ApiService.common.serializers import PositionSerializer
#For Rest Based Views
# Create your views here.
# https://www.django-rest-framework.org/api-guide/views/

class ValidPosition(generics.ListAPIView):
    serializer_class = PositionSerializer
    lookup_url_kwarg = "ticker"

    def get_queryset(self):
        positions=[]
        if(self.kwargs.__contains__('ticker')):
            positions = Numberid.objects.filter(tickersymbol=self.kwargs['ticker'])
        elif(self.kwargs.__contains__('callsOrPuts')):
            positions = self.getPutOrCall(self.kwargs['callsOrPuts'])
        return positions

    @staticmethod
    def getPutOrCall(putOrCall):
        if((putOrCall == "calls") or (putOrCall == "call")):
            return Numberid.objects.filter(iscall=1)
        if((putOrCall == "puts") or (putOrCall == "put")):
            return Numberid.objects.filter(iscall=0)
