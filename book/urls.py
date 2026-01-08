from rest_framework.routers import DefaultRouter
from .views import BookView
from django.urls import path, include
router = DefaultRouter()
router.register('books', BookView, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]