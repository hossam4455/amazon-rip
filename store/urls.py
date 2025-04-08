from django.urls import path, include
from rest_framework_nested import routers
from .views import ProductViewSet, CollectionViewSet, ReviewViewSet,CartViewSet,CartItemViewSet

# Primary router
router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('collections', CollectionViewSet)
router.register('carts',CartViewSet)
router.register('cartitems',CartItemViewSet)
# Nested router for reviews under products
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')

# Combine URLs
urlpatterns = router.urls + products_router.urls