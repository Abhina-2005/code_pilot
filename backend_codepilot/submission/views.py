from django.shortcuts import render

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView

from rest_framework import authentication,permissions

from assessment.models import Assessment

from submission.models import Submission

from assessment.Permissions import OwnerOnly

from submission.serializers import SubmissionSerializer

from submission.permissions import IsOwner,AdminOnly

from rest_framework.views import APIView

from rest_framework.response import Response

from django.utils import timezone

class SubmissionCreateView(CreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def perform_create(self, serializer):

        return serializer.save(student=self.request.user)
    

class SubmissionListView(ListAPIView):

    serializer_class = SubmissionSerializer

    queryset = Submission.objects.all()

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [OwnerOnly]


class SubmissionRetrieveView(RetrieveAPIView):

    serializer_class = SubmissionSerializer

    queryset = Submission.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

class SubmissionStatusView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, pk):

        try:
            submission = Submission.objects.get(id=pk,student=request.user)

            return Response({

                "submission_id": submission.id,

                "status": submission.status,

                "evaluation_status": submission.evaluation_status
            })

        except Submission.DoesNotExist:

            return Response({

                "message": "Submission not found"

            })

class SubmissionFinalAssessmentView(UpdateAPIView):

    serializer_class = SubmissionSerializer

    queryset = Submission.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    def patch(self, request, pk):

        try:
            submission = Submission.objects.get(id=pk,student=request.user)

            submission.status = "submitted"

            submission.submitted_at = timezone.now()

            submission.save()

            return Response({

                "message": "Assessment submitted successfully",

                "status": submission.status
            })

        except Submission.DoesNotExist:

            return Response({

                "message": "Submission not found"

            })

class SubmissionEvaluateView(UpdateAPIView):

    serializer_class = SubmissionSerializer

    queryset = Submission.objects.all()

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [AdminOnly]

    def patch(self, request, pk):

        try:
            submission = Submission.objects.get(id=pk)

            submission.total_marks = request.data.get(

                "total_marks",

                submission.total_marks
            )

            submission.evaluation_status = "evaluated"

            submission.save()

            return Response({

                "message": "Submission evaluated successfully",

                "submission_id": submission.id,

                "total_marks": submission.total_marks,

                "evaluation_status": submission.evaluation_status

            })

        except Submission.DoesNotExist:

            return Response({

                "message": "Submission not found"

            })





















