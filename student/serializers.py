from rest_framework import serializers
from .models import Student_account

class StudentAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_account
        fields = '__all__'