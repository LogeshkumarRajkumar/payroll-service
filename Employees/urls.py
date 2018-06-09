from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<employee_id>.*)/$', views.EmployeeDetails.as_view(), name='detail'),
]
