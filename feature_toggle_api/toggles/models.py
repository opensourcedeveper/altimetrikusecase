from django.db import models
from django.contrib.auth.models import User

class FeatureToggle(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    notes = models.TextField(blank=True)
    is_enabled = models.BooleanField(default=False)
    environment = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
