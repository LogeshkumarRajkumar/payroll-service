from django.conf.urls import url

from . import views

urlpatterns = [
    url('register/', views.CompanyDetail.as_view(), name='detail'),
]
