from django.db import models
import uuid
from Employees.models import EmployeeType
from Clients.models import Client
from Companies.models import Company
from Common.Validators import validate_alpha_numeric


class Employee(models.Model):
    id = models.CharField(max_length=200, primary_key=True, default=uuid.uuid4, editable=True)
    name = models.CharField(max_length=200, validators=[validate_alpha_numeric], blank=False)
    salary = models.FloatField(blank=False)
    employeeType = models.ForeignKey(EmployeeType, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
