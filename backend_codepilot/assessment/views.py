from django.shortcuts import render

# # Create your views here.

from assessment.serializers import AssessmentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from assessment.models import Assessment
from rest_framework import authentication,permissions
from assessment.Permissions import OwnerOnly

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status


class AssessmentListCreateView(ListCreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    queryset=Assessment.objects.all() 
    serializer_class=AssessmentSerializer

    def get_queryset(self):
        return Assessment.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class AssessmentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]
    
    serializer_class=AssessmentSerializer

    queryset=Assessment.objects.all()   
     
class AssessmentPublishview(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]

    def post(self,request,pk):
        assessment=Assessment.objects.get(pk=pk)
        assessment.status=True
        assessment.save()

        return Response(
            {
                "message":"Assessment published successfully",
                "status":assessment.status
            },
            status=status.HTTP_200_OK
        )





    