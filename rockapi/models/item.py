from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collection')
    location = models.ForeignKey("Location", on_delete=models.CASCADE, related_name='rocks')
    name = models.CharField(max_length=155)
    amount = models.DecimalField(max_digits=5, decimal_places=2)