from rest_framework import generics
from .serializer import bandserializer
from .models import Bands
from .permissions import IsOwnerOrReadOnly

class BandsList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = bandserializer
    queryset = Bands.objects.all()

class BandsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = bandserializer
    queryset = Bands.objects.all()
