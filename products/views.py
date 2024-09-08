from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from rest_framework import generics

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BusinessProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        business_id = self.kwargs['business_id']
        return Product.objects.filter(user__business_id=business_id)