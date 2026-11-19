from django.urls import path

from questions.views import QuestionListCreateView

urlpatterns = [

    path("assessment/assessment_id/question/",QuestionListCreateView.as_view()),
    
]