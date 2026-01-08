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
            serializer.save()
            return Response("Student account created successfully")
        return Response(serializer.errors, status=400)