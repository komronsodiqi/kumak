from django.contrib import admin
from django.urls import path
from category.views.cbv import CategoryListAPIView, CategoryDetailAPIView, ProductListAPIView, ProductDetailAPIView
from category.views.fbv import category_products
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny


@api_view(['GET'])
def api_root(request):
    return Response({"message": "Welcome to the API!"})

class PublicTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]

urlpatterns = [
    path('', api_root),
    path('login/', PublicTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),
    path('categories/<int:category_id>/products/', category_products),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()),
]