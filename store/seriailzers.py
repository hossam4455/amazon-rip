from rest_framework import serializers
from .models import Product , Collection ,Review
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
       product_id=self.context['product_id']
       return  Review.objects.create(product_id=product_id,**validated_data)
       