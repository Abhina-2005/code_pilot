from django.shortcuts import render

# Create your views here.
from submission.models import Submission

from assessment.models import Assessment

from django.shortcuts import get_object_or_404

from submission.serializers import SubmissionSerializer 

from rest_framework import authentication,permissions

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView

from submission.permissions import IsOwner

from assessment.Permissions import OwnerOnly


from rest_framework.response import Response


class SubmissionCreateView(CreateAPIView):

    serializer_class=SubmissionSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def perform_create(self, serializer):

        assessment = get_object_or_404(Assessment,id=self.kwargs['pk'])

        serializer.save(student=self.request.user,assessment=assessment)



class SubmissionListView(ListAPIView):

    serializer_class=SubmissionSerializer

    queryset=Submission.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwner]

   

class SubmissionRetrieveView(RetrieveAPIView):

    serializer_class=SubmissionSerializer

    queryset=Submission.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwner]

    


class SubmissionStatusView(RetrieveAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwner]

    def get(self,request,pk):

        try:
            submission=Submission.objects.get(id=pk,student=request.user)

            return Response({

                "submission_id": submission.pk,

                "status": submission.status
            })
        except Submission.DoesNotExist:

            return Response({

                 "message": "Assessment not submitted yet"
            })

class SubmissionFinalAssessmentView(CreateAPIView):

    serializer_class = SubmissionSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwner]

    def post(self,request,pk):

        try:
            submission=Submission.objects.get(id=pk,student=request.user)

            submission.status="submitted"

            submission.save()

            return Response({

                "message": "Assessment submitted successfully",

                "status": submission.status

            })
        
        except Submission.DoesNotExist:

            return Response({

                "message": "Submission not found"
            })


class SubmissionEvaluateView(RetrieveAPIView):

    serializer_class = SubmissionSerializer

    queryset = Submission.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def post(self, request, pk):

        try:
            submission = Submission.objects.get(id=pk)

            submission.marks = request.data.get("marks")

            submission.feedback = request.data.get("feedback")

            submission.status = "evaluated"

            submission.save()

            return Response({

                "message": "Assessment evaluated successfully",

                "submission_id": submission.pk,

                "marks": submission.marks,

                "feedback": submission.feedback,

                "status": submission.status
            })

        except Submission.DoesNotExist:

            return Response({
                
                "message": "Submission not found"
            })

            
        