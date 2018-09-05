from django.db import models
import uuid
from Companies.models import Company
from Common.Validators import validate_alpha_numeric


class EmployeeType(models.Model):
    id = models.CharField(max_length=200, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, validators=[validate_alpha_numeric], blank=False)
    salaried = models.BooleanField(blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class EmployeeTypeDetails(models.Model):
    employeeType = models.ForeignKey('EmployeeType', on_delete=models.CASCADE)
    startTime = models.IntegerField(blank=False)
    endTime = models.IntegerField(blank=False)
    wageMultiple = models.FloatField(max_length=4, default=1, blank=False)
