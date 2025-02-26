from django.shortcuts import render, get_object_or_404
from tecno_store.apps.products.models import Product

# Create your views here.
def product_details(request, product_id):
    # Obtener el producto por su ID o mostrar un error 404 si no existe
    product = get_object_or_404(Product, id=product_id)
    
    # Pasar el producto al contexto
    context = {
        'product': product
    }
    return render(request, 'products/product_details.html', context)