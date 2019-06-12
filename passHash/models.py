from django.db import models

# Create your models here.
class Usertb(models.Model):
	username = models.CharField(max_length=50,unique=True)
	passhash = models.CharField(max_length=1000,null=True)
	
	def __str__(self):
		return self.username
		