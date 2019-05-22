
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','x0','y0','x1','y1','x2','y2','x3','y3','image','image_url','passhash')

		extra_kwargs = {"username": {"read_only": True},
                        "x0": {"read_only": True},
                        }


