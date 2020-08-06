# from  import Numberid, TickersTable
from rest_framework import generics


#For Rest Based Views
# Create your views here.
# https://www.django-rest-framework.org/api-guide/views/

class Account(generics.ListAPIView):

    # serializer_class = PositionSerializer
    # lookup_url_kwarg = "ticker"
    #
    def get_queryset(self):
        return self.get_hello(self)

    def get_hello(self):
        positions=[]
        # if(self.kwargs.__contains__('ticker')):
        #     positions = Numberid.objects.filter(tickersymbol=self.kwargs['ticker'])
        # elif(self.kwargs.__contains__('callsOrPuts')):
        #     positions = self.getPutOrCall(self.kwargs['callsOrPuts'])
        return "hello"
    #
    # @staticmethod
    # def getPutOrCall(putOrCall):
    #     if((putOrCall == "calls") or (putOrCall == "call")):
    #         return Numberid.objects.filter(iscall=1)
    #     if((putOrCall == "puts") or (putOrCall == "put")):
    #         return Numberid.objects.filter(iscall=0)

