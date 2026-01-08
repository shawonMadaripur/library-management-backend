from django.shortcuts import render
from rest_framework import viewsets
from .models import Purchase_info
from .serializers import PurchaseInfoSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class PurchaseInfoViewSet(viewsets.ModelViewSet):
    queryset = Purchase_info.objects.all()
    serializer_class = PurchaseInfoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('student_id', None)
        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"error": "Student not found."}, status=404)
        return super().list(request, *args, **kwargs)
    
class DeletePurchaseInfoView(APIView):
    def delete(self, request, pk):
        try:
            purchase_info = Purchase_info.objects.get(pk=pk)
            purchase_info.delete()
            return Response(status=204)
        except Purchase_info.DoesNotExist:
            return Response({"error": "Purchase info not found."}, status=404)
    

class StudentPurchaseInfoPIView(APIView):
    def post(self, request):
        serializer = PurchaseInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)