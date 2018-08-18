from rest_framework.views import APIView, Response
from DHT.models import DHTModel
from audio.models import AbnormalityModel
from django.utils import timezone
from datetime import timedelta


class StatusView(APIView):

    def get(self, request):

        dht = DHTModel.objects.order_by("-date_time").first()

        abnorm = AbnormalityModel.objects.filter(date_time__gte=timezone.now() - timedelta(seconds=5)).exists()

        return Response(dict(
            abnorm=abnorm,
            humid=int(dht.humid),
            temp=int(dht.temp)
        ), 200)
