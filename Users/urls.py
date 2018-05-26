from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.CompanyDetail.as_view(), name='detail'),
]
