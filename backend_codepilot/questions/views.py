from django.shortcuts import render,get_object_or_404

# Create your views here.

from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework import authentication,permissions

from questions.permissions import Owneronly

from  questions.serializers import QuestionSerializer

from questions.models import Question
from assessment.models import Assessment

class QuestionListCreateView (CreateAPIView,ListAPIView) :

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [Owneronly]

    serializer_class = QuestionSerializer

    def get_queryset(self):
        return Question.objects.filter(
        assessment_id=self.kwargs['pk'],
        assessment__creator=self.request.user
    )

    #def perform_create(self, serializer):
    #return serializer.save()

    def perform_create(self, serializer):
        assessment = get_object_or_404(
            Assessment,
            id=self.kwargs['pk'],
            creator=self.request.user
        )

        serializer.save(assessment=assessment)

class QuestionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [Owneronly]
    serializer_class = QuestionSerializer

    # quesryset = Question.objects.all()

    def get_queryset(self):
        return Question.objects.filter(
            assessment__creator=self.request.user
        )
