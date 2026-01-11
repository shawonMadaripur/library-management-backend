from rest_framework.routers import DefaultRouter
from .views import PurchaseInfoViewSet, StudentPurchaseInfoPIView, DeletePurchaseInfoView
from django.urls import path, include
router = DefaultRouter()
router.register('purchase_info', PurchaseInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('purchase_info_submit/', StudentPurchaseInfoPIView.as_view(), name='purchase_info_submit'),
    path('purchase_info_delete/<int:pk>/', DeletePurchaseInfoView.as_view(), name='purchase_info_delete'),
]
