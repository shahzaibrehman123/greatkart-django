from django.http import HttpResponse
from django.shortcuts import render
from store.models import product

def home(request):
    products = product.objects.all().filter(is_available=True)

    context = {

        'product': products
    }


    return render(request,'home.html', context)