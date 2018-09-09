from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.EmployeeDetails.as_view(), name='detail'),
]
