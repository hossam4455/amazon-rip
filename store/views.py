from django.shortcuts import get_object_or_404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet ,GenericViewSet
from .models import Product, Collection ,OrderItem ,Review,Cart,CartItem
from .seriailzers import ProductSerializer, CollectionSerializer,ReviewSerializer,CartSerializer,CartItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter ,OrderingFilter
from rest_framework.pagination import PageNumberPagination


class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend ,SearchFilter,OrderingFilter]
    filterset_fields=['collection_id']
    search_fields=['title','description','collection__title']
    ordering_fields = ['price','last_update']
    def get_serializer_context(self):
        return {'request':self.request}
    def destroy(self, request, *args, **kwargs):

        if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
            return Response(
                {'error': 'Cannot delete a product linked to order items'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )  
        return super().destroy(request, *args, **kwargs)

class CollectionViewSet(ModelViewSet):
    queryset=Collection.objects.all()
    serializer_class=CollectionSerializer
    def get_serializer_context(self):
        return {'request':self.request}
    def destroy(self, request, *args, **kwargs):

        if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
            return Response(
                {'error': 'Cannot delete a product linked to order items'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )  
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    
    serializer_class=ReviewSerializer
    def get_serializer_context(self):
        return {'product_id':self.kwargs['product_pk']}
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    


class CartViewSet(CreateModelMixin,GenericViewSet):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer

class CartItemViewSet(ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
