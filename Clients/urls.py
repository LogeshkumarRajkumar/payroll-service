
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ClientDetails.as_view({'get':'list', 'post':'post'}), name='detail'),
    url(r'^(?P<client_id>.*)/$', views.ClientDetails.as_view({'get': 'get', 'put':'put'}), name='detail'),
]
