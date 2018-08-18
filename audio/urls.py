from django.conf.urls import url
from .views import AbnormalityView, UploadView, LollyView


urlpatterns = [
    url(r'^append/', AbnormalityView.as_view()),
    url(r'^upload/', UploadView.as_view()),
    url(r'^lolly/(?P<id>\d+)?/$', LollyView.as_view())
]
