from django.db import models
from django.db.models.base import Model

# Create your models here.

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(False)
    is_favorite = models.BooleanField(False)
