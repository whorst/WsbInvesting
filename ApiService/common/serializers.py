from ApiService.common.models import Numberid
from rest_framework import serializers


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Numberid
        fields = ['idnumberid', 'dateadded', 'expirydate', 'iscall', 'tickersymbol']