from rest_framework import serializers
from .models import Dht

class DhtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dht
        fields = '__all__'