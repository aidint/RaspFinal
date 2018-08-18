# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from rest_framework.views import APIView, Response
from .models import DHTModel
from.serializers import DHTSerializer
# Create your views here.


class DHTView(APIView):

    def post(self, request):

        data = request.data
        temp = data["temp"]
        humid = data["humid"]
        time = timezone.now()

        dht = DHTModel(temp=temp, humid=humid, date_time=time)
        dht.save()

        if DHTModel.objects.count() > 2000:

            DHTModel.objects.order_by("date_time")[:1000].delete()

        return Response(DHTSerializer(dht).data, 200)


class ReceiveView(APIView):

    def post(self, request):

        data = request.data

        number = data["number"] if "number" in data else 1

        dhts = DHTModel.objects.order_by('-date_time')[:number]

        return Response(DHTSerializer(dhts, many=True).data, 200)




