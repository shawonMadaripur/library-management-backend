from .views import StudentAccountView
from django.urls import path

urlpatterns = [
    path('student_account/', StudentAccountView.as_view(), name='student_account'),
]
