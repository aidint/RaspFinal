from rest_framework import serializers
from .models import DHTModel


class DHTSerializer(serializers.ModelSerializer):

    class Meta:

        model = DHTModel
        fields = ("date_time", "humid", "temp")
