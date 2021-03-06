import cv2
import numpy as np
import sys
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from urllib.request import Request, urlopen
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from django.conf import settings
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# Create your views here.
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.generics import GenericAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.renderers import (
                                        HTMLFormRenderer, 
                                        JSONRenderer, 
                                        BrowsableAPIRenderer,
                                    )

from .models import Usertb
from .serializers import UserSerializer

class UserRetrieveView(GenericAPIView):
	permission_classes = []
	queryset=Usertb.objects.all()
	serializer_class=UserSerializer
	lookup_field='username'
	lookup_url_kwarg = 'username'

	def post(self, request, *args, **kwargs):
		print("self : ", self)
		print("request : ", request.data)
		try:
			UserObject = Usertb.objects.get(username=request.data['username'])
			if UserObject:
				serializer = self.get_serializer(data=request.data)
				serializer.is_valid(raise_exception=True)
				x0=request.data['x0']
				y0=request.data['y0']
				x1=request.data['x1']
				y1=request.data['y1']
				x2=request.data['x2']
				y2=request.data['y2']
				x3=request.data['x3']
				y3=request.data['y3']
				image_url=request.data['image_url']
				passhash=hash_function(image_url,x0,y0,x1,y1,x2,y2,x3,y3)
				print("UserObject : " ,UserObject)
				if passhash==UserObject.passhash:
					ctx={'username':request.data['username']}
					return Response(ctx, status=status.HTTP_200_OK)
				else:
					return Response({'username':False}, status=status.HTTP_401_UNAUTHORIZED)
		
		except ObjectDoesNotExist:
			return Response({'username':False}, status=status.HTTP_404_NOT_FOUND)
		
		
		
	
	def get_queryset(self):
		user = Usertb.objects.filter(username=self.kwargs['username'])
		print("user in get query",user)
		return user

class UserCreateView(CreateAPIView):
	permission_classes = []
	queryset = Usertb.objects.all()
	serializer_class = UserSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		
		serializer.validated_data['passhash']= hash_function(serializer.validated_data['image_url'],
				serializer.validated_data['x0'],serializer.validated_data['y0'],
				serializer.validated_data['x1'],serializer.validated_data['y1'],
				serializer.validated_data['x2'],serializer.validated_data['y2'],
				serializer.validated_data['x3'],serializer.validated_data['y3'],			
			)
		try:
			Usertb.objects.get(username=serializer.validated_data['username'])
			return Response({'username':False}, status=status.HTTP_406_NOT_ACCEPTABLE)
		except ObjectDoesNotExist:
			Usertb.objects.create(username=serializer.validated_data['username'],passhash=serializer.validated_data['passhash'])
			headers = self.get_success_headers(serializer.data)
			print(headers)
			return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
			



def url_to_image(url):
	resp = urlopen(url).read()
	image = np.asarray(bytearray(resp),dtype="uint8")
	image = cv2.imdecode(image,cv2.IMREAD_COLOR)
	return image

def hashing_algo(im,X0,Y0,X1,Y1,X2,Y2,X3,Y3):
	xarr=[int(X0),int(X1),int(X2),int(X3)]
	yarr=[int(Y0),int(Y1),int(Y2),int(Y3)]
	print(xarr)
	print(yarr)
	passhash=""
	for (x,y) in zip(xarr,yarr):
			print("coordinates : ",x,"\t",y)
			dmc = im[x-50:x+50, y-50:y+50]
			gray= cv2.cvtColor(dmc,cv2.COLOR_BGR2GRAY)
			sift = cv2.xfeatures2d.SIFT_create(1)
			key = sift.detect(gray,None)
			img=cv2.drawKeypoints(gray,key,im)
			img1=cv2.drawKeypoints(gray,key,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
			key,des=sift.compute(gray,key)

			if des is None:
				des=np.zeros(128)
				print(des)
				for each in des:
					if int(each)==0:
						passhash+='b'
					else:
						passhash+=str(int(each))
				continue

			single_des=des[0]
			print(single_des)
			for each in single_des:
				if int(each)==0:
					passhash+='b'
				else:
					passhash+=str(int(each))

	print("passhash",passhash)
	print("passhash length",len(passhash))
	return passhash
	hash=""
	# while passhash!="":
	# 	hash+=chr(int(passhash[:2]))
	# 	passhash=passhash[2:]
	# print(hash)

def hash_function(image_url,x0,y0,x1,y1,x2,y2,x3,y3):
	req=Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
	print("Downloading %s"%(req))
	im=url_to_image(req)
	print(im.shape)
	return hashing_algo(im,x0,y0,x1,y1,x2,y2,x3,y3)





