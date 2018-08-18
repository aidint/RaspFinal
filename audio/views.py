# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import Response, APIView
from .models import AbnormalityModel
from django.utils import timezone
from .serializers import FileSerializer
import pyaudio
import wave
import time
from Final.settings import BASE_DIR
import after_response
from django.core.cache import cache
import numpy as np
import audioread
import io
# Create your views here.


@after_response.enable
def play_file(file_name, id=0):

    # create an audio object
    wf = wave.open(file_name, 'rb')
    p = pyaudio.PyAudio()
    chunk = 1024
    redis_key = "stop-%d" % id

    if cache.get(redis_key):
        cache.delete(redis_key)

    def callback(in_data, frame_count, time_info, status):

        if cache.get(redis_key):

            stream.stop_stream()
            stream.close()
            wf.close()

            p.terminate()
            return

        data = wf.readframes(frame_count)
        return data, pyaudio.paContinue

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)


    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()


class AbnormalityView(APIView):

    def get(self, request):
        AbnormalityModel.objects.create(date_time=timezone.now())
        return Response({}, 200)


class UploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        file_serialized = FileSerializer(data=request.data)

        file_serialized.is_valid(raise_exception=True)

        cache.set("stop-1", 1)

        cache.set("stop-2", 1)

        cache.set("stop-3", 1)

        file_serialized.save(is_checked=True)

        play_file.after_response(BASE_DIR + file_serialized.data["file"])

        return Response(file_serialized.data, 200)


class LollyView(APIView):

    def get(self, request, *args, **kwargs):

        id = int(kwargs["id"]) if "id" in kwargs else 1

        try:
            play_file.after_response(BASE_DIR + "/music/%d.wav" % id, id)

            return Response({}, 200)

        except:

            return Response({}, 400)

    def delete(self, request, *args, **kwargs):

        id = int(kwargs["id"]) if "id" in kwargs else 1

        cache.set("stop-%d" % id, 1)

        return Response({}, 200)
