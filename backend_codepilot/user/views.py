
from django.shortcuts import render

# from rest_framework.views import APIView

# from rest_framework.authtoken.views import ObtainAuthToken

# from user.models import User,StudentProfile

from user.serializers import AdminSerializer,StudentSerializer

from rest_framework.generics import CreateAPIView

class AdminCreateView(CreateAPIView):

    serializer_class = AdminSerializer


class StudentCreateView(CreateAPIView):

    serializer_class = StudentSerializer

    

