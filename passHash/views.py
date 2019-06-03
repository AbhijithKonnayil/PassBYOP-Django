from django.shortcuts import render
from rest_framework.response import Response
from django.conf import settings
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# Create your views here.
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.renderers import (
                                        HTMLFormRenderer, 
                                        JSONRenderer, 
                                        BrowsableAPIRenderer,
                                    )

from .models import User
from .serializers import UserSerializer


class UserView(APIView):
	permission_classes = []
#	renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
	def get(self,request):
		userlist=User.objects.filter(username="abhi")
		print(userlist)
		serializer = UserSerializer(
		userlist, many=True, context={'akshay':"bharat"})
		pass_data = serializer.data
		print(" \nBR", settings.BASE_DIR, " \n");
		print(" \nSD", settings.STATICFILES_DIRS, " \n");
		print(" \nSR", settings.STATIC_ROOT, " \n");
		pass_data_dict = pass_data[0]
		return Response(pass_data_dict, status=HTTP_200_OK)
	
	# def post(self, request):
	# 	print(Response())
	# 	return Response()

	def post(self, request,**kwargs):
		data = request.data
		print("DATA : ",data)
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



		# class AgentLoginAPIView(APIView):

  #   permission_classes = [AllowAny]
  #   serializer_class = AgentLoginSerializer

  #   def post(self, request, **kwargs):
  #       phone = data.get('phone')
  #       password = data.get('password')
  #       agent = Agent.objects.filter(phone__icontains=phone).first()
  #       if agent:
  #           authenticate(username=agent.username, password=password)
  #           serializer = AgentLoginSerializer(agent)
  #           if agent.is_authenticated:
  #               login(request, agent)
  #               return Response(serializer.data, status=HTTP_200_OK)
  #           else:
  #               return Response(status=HTTP_400_BAD_REQUEST)
  #       return Response(status=HTTP_400_BAD_REQUEST)
