from rest_framework import serializers
from myrestapi.models import Dht

class DhtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dht
        fields = ('temp', 'hum', 'dt')