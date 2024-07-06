from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Travel, Sayohat_turi
from .serializers import TravelSerializer, SayohatSerializer
from .permission import SayohatPermission, TravelPermission

class TravelAPIView(ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [TravelPermission]

class SayohatTuriAPIView(ModelViewSet):
    queryset = Sayohat_turi.objects.all()
    serializer_class = SayohatSerializer
    permission_classes = [SayohatPermission]