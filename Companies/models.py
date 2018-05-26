from django.db import models
from django.conf import settings
import uuid


class Company(models.Model):
    id = models.CharField(max_length=20000, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20000)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
