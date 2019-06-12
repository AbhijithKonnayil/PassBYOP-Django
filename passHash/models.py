from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50,unique=True);
	x0=models.IntegerField()
	y0=models.IntegerField()
	x1=models.IntegerField()
	y1=models.IntegerField()
	x2=models.IntegerField()
	y2=models.IntegerField()
	x3=models.IntegerField()
	y3=models.IntegerField()
	image_url=models.CharField(max_length=1000,null=True)
	passhash = models.CharField(max_length=1000,null=True)
	
	def __str__(self):
		return self.username
		