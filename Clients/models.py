from django.db import models
import uuid
from Companies.models import Company
from Common.Validators import validate_alpha_numeric


class Client(models.Model):
    id = models.CharField(max_length=200, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, validators=[validate_alpha_numeric], blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

