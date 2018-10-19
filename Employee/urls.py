
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.EmployeeDetails.as_view({'get':'list', 'post':'post'}), name='detail'),
    url(r'^(?P<employee_id>.*)/$', views.EmployeeDetails.as_view({'get': 'get', 'put':'put'}), name='detail'),
]
