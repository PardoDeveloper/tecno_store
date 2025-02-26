from django.shortcuts import render
from tecno_store.apps.products.models import Product

# Create your views here.
def index(request):
    # Obtener todos los productos
    products = Product.objects.all()
    
    # Pasar los productos al contexto
    context = {
        'products': products
    }
    return render(request, 'home/index.html', context)


def productos(request):
    products = Product.objects.all()
    data = {
        "products": products
    }
    return render(request, 'products/products.html', data)