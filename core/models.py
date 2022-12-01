from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
from django.conf import settings
from accounts.models import *
# from accounts import models

User = get_user_model()

class Category(models.Model):
    category_name =models.CharField(max_length=20)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name


class Policy(models.Model):
    email=models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    category= models.ForeignKey('Category', on_delete=models.CASCADE)
    policy_name=models.CharField(max_length=200)
    sum_assurance=models.PositiveIntegerField()
    premium=models.PositiveIntegerField()
    tenure=models.PositiveIntegerField()
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.policy_name
