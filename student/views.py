from django.shortcuts import render
from .models import Student_account
from .serializers import StudentAccountSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class StudentAccountView(APIView):
    def post(self, request):
        serializer = StudentAccountSerializer(data=request.data)
        if serializer.is_valid():

            student_id = serializer.validated_data.get('student_id')
            # Check if student already exists
            if Student_account.objects.filter(student_id=student_id).exists():
                return Response("Student account with this ID already exists", status=400)
            
            serializer.save()
            return Response("Student account created successfully")
        return Response(serializer.errors, status=400)