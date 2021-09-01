from django.urls import path
from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products', ProductViewSet.as_view({
      'get': 'list',
      'post': 'create'
    })),

    path('products/<str:primary_key>', ProductViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'delete': 'destroy',
    })),

    path('user', UserAPIView.as_view())
]