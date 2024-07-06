from rest_framework import serializers

from .models import Sayohat_turi, Travel

class SayohatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sayohat_turi
        fields = '__all__'


class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'