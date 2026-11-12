
from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.authtoken.views import ObtainAuthToken

from user.models import User,StudentProfile

from user.serializers import AdminSerializer,StudentSerializer,StudentProfileSerializer

from rest_framework.generics import CreateAPIView

class AdminCreateView(CreateAPIView):

    serializer_class = AdminSerializer

class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = AdminSerializer(data=form_data)



