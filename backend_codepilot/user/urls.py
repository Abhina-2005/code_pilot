
from django.urls import path,include
from user.views import AdminCreateView,StudentCreateView

urlpatterns = [

    path('admin/register/',AdminCreateView.as_view()),
    path('student/register/',StudentCreateView.as_view()),

]
