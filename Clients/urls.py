
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ClientDetails.as_view(), name='detail'),
]
