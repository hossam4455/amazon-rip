from django.shortcuts import render
from store.models import Product, OrderItem

def say_hello(request):
    # Get a list of distinct product IDs
    product= Product.objects.defer('id','title')
    
    # Filter OrderItems where product_id is in the list of product_ids
  
    return render(request, 'hello.html', {'name': 'mosh', 'product':list( product)})