from django.urls import path

from assessment.views import AssessmentListCreateView,AssessmentRetrieveUpdateDeleteView,AssessmentPublishview

urlpatterns = [

    path('exam/',AssessmentListCreateView.as_view()),
    path('exam/<int:pk>/',AssessmentRetrieveUpdateDeleteView.as_view()),
    path("exam/<int:pk>/publish/",AssessmentPublishview.as_view()),

]