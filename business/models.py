from django.db import models
from users.models import CustomUser

class Business(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)

