from django.urls import path, include

from rest_framework.routers import DefaultRouter

from expenses.views import UserViewSet, ExpenseViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
]
