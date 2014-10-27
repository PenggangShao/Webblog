#coding=utf-8
from django.db import models
class User(models.Model):
	user_name=models.CharField(max_length=30)
	user_pass=models.CharField(max_length=30)
	user_email=models.CharField(max_length=50)
