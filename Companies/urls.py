from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.CompanyDetail.as_view(), name='detail'),
]
