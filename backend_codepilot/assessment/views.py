from django.shortcuts import render

# # Create your views here.

from assessment.serializers import AssessmentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from assessment.models import Assessment


class AssessmentListCreateView(ListCreateAPIView):
    serializer_class=AssessmentSerializer
    queryset = Assessment.objects.all()


class AssessmentRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AssessmentSerializer
    queryset = Assessment.objects.all()



    