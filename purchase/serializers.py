from rest_framework import serializers
from .models import Purchase_info

class PurchaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase_info
        fields = '__all__'