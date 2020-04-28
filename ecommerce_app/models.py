from django.db import models
from django.contrib import messages
import re


class Reviews(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

