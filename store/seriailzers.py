from rest_framework import serializers
from .models import Product , Collection ,Review,Cart,CartItem
from decimal import Decimal

class CollectionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)
class ProductSerializer(serializers.Serializer):
 
    id=serializers.IntegerField()
    description=serializers.CharField()
    title=serializers.CharField(max_length=255)
    price=serializers.DecimalField(max_digits=6,decimal_places=2)
    price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.HyperlinkedRelatedField(
    queryset=Collection.objects.all(),  # ✅ correct key
    view_name='collection-detail'       # ✅ make sure view name is correct
    )
    def calculate_tax(self,product:Product):
        return product.price*Decimal(1.1)
    
class CollectionSerializer(serializers.ModelSerializer):
        products_count = serializers.IntegerField(read_only=True)
    
        class Meta:
         model = Collection
         fields = ['id', 'title', 'products_count']

class ReviewSerializer(serializers.ModelSerializer):
   class Meta:
      model=Review
      fields=['id','date','name','description']
   def create(self, validated_data):
       print('sss',self.context['product_id'])
       product_id=self.context['product_id']
       
       return  Review.objects.create(product_id=product_id,**validated_data)

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'qunantity']
class SimpelCartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['product', 'qunantity', 'total_price']

    def get_total_price(self, obj):
        return obj.product.price * obj.qunantity
class CartSerializer(serializers.ModelSerializer):
    items = SimpelCartItemSerializer(many=True, read_only=True)
    id = serializers.UUIDField(read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'created_at', 'items', 'total']

    def get_total(self, cart):
        return sum([
            item.product.price * item.qunantity
            for item in cart.items.all()
        ])