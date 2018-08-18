from django.conf.urls import url
from .views import DHTView, ReceiveView


urlpatterns = [
    url(r'^send/', DHTView.as_view()),
    url(r'^receive/', ReceiveView.as_view())
]
