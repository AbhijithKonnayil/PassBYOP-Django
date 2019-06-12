
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','x0','y0','x1','y1','x2','y2','x3','y3','image_url','passhash')



