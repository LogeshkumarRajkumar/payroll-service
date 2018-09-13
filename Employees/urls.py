from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.EmployeeDetails.as_view({'get':'list', 'post':'post'}), name='detail'),
    url(r'^(?P<employee_typeid>.*)/$', views.EmployeeDetails.as_view({'get': 'get',}), name='detail'),
    url(r'^(?P<employee_typeid>.*)/wage-details$', views.WageDetails.as_view({'get': 'list', }), name='detail'),
]
