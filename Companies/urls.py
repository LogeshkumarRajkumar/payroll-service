from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^(?P<company_id>.*)/employee-types/', include('Employees.urls'), name='detail'),
    url(r'^(?P<company_id>.*)/$', views.CompanyDetail.as_view(), name='detail'),
]
