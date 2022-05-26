from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductListSerializer, ProductSerializer, ProductCRUDSerializer


class ProductAPIView(APIView):
    def get(self, request):
        search = request.query_params.get("search")
        if search:
            products = Product.objects.filter(Q(title__icontains=search) | Q(desc__icontains=search), is_published=True)
        else:
            products = Product.objects.filter(is_published=True)
        products = products.order_by('title', 'price')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductSetView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCRUDSerializer
