
from rest_framework import serializers
from .models import Usertb

class UserSerializer(serializers.Serializer):
	username=serializers.CharField(max_length=50)
	x0=serializers.IntegerField()
	y0=serializers.IntegerField()
	x1=serializers.IntegerField()
	y1=serializers.IntegerField()
	x2=serializers.IntegerField()
	y2=serializers.IntegerField()
	x3=serializers.IntegerField()
	y3=serializers.IntegerField()
	image_url=serializers.CharField(max_length=1000)


