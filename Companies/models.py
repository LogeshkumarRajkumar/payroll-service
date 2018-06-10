from django.db import models
from django.conf import settings
import uuid
from Common.Validators import validate_alpha_numeric


class Company(models.Model):
    id = models.CharField(max_length=20000, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20000, validators=[validate_alpha_numeric])
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
