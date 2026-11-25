from django.urls import path

from questions.views import QuestionListCreateView
from  questions.views import QuestionRetrieveUpdateDeleteView

urlpatterns = [

    path("assessment/<int:pk>/task/",QuestionListCreateView.as_view()),
    path("task/<int:pk>/",QuestionRetrieveUpdateDeleteView.as_view()),
    
]