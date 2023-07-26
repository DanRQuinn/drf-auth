from rest_framework import serializers
from .models import Bands

class bandserializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'members', 'created_at', 'updated_at')
        model = Bands


