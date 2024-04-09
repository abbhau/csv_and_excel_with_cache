from django.urls import path
from .views import StudentView, StudentList

urlpatterns =[
    path('caches/', StudentView.as_view(), name="cache"),
    path('student/', StudentList.as_view(), name="student-list")
]