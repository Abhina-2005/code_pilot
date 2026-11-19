from django.urls import path

from assessment.views import AssessmentListCreateView,RetrieveUpdateDestroyAPIView

urlpatterns = [

    path("assessment/",AssessmentListCreateView.as_view()),
    path('assessment/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view()),
]
