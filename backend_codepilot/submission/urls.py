from django.urls import path

from submission.views import (SubmissionCreateView,SubmissionListView,SubmissionRetrieveView,SubmissionStatusView,
SubmissionFinalAssessmentView,SubmissionEvaluateView)

urlpatterns = [
    
    path("assessment/<int:pk>/submissions/",SubmissionCreateView.as_view()),

    path("submissions/ ",SubmissionListView.as_view()),
   
    path("<int:pk>/",SubmissionRetrieveView.as_view()),

    path("submissions/<int:pk>/status/",SubmissionStatusView.as_view()),

    path("submissions/<int:pk>/submit/",SubmissionFinalAssessmentView.as_view()),

    path("submissions/<int:pk>/evaluate/",SubmissionEvaluateView.as_view()),
]

