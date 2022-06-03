from django.shortcuts import render
from .models import Product,Currency
from django.contrib.auth.models import User
from django.http import Http404
import requests,json

def index(request):
    products = Product.objects.all()[::-1]
    user=User.objects.get(id=1)
    context= {
        "name":"Vasyl",
        "company_name":"Phone Store",
        "products":products,
        "cart_link":'cart/',
    }
    return render(request=request,template_name='store/index.html',context=context)

def product(request):
    if request.method=='GET':
        product_id = request.GET.get("prod", "")
        try:
            product = Product.objects.get(id=product_id)
        except:
            raise Http404("Wrong path!")

        all_curr=Currency.objects.all()
        url="https://api.exchangerate-api.com/v4/latest/USD"
        response=requests.get(url)
        result=response.json()
        price=dict()
        for curr in all_curr:
            price[curr.cur_name]=f"{curr.character} {int(result['rates'][curr.cur_name]*product.price_USD)}"
        context={
            "company_name": "PHONE STORE",
            "product":product,
            "cart_link": "/cart/",
            "price":price,
        }
        return render(request=request, template_name='store/product.html', context=context)


def cart(request):
    if request.method == 'GET':
        context={
            "company_name": "PHONE STORE",
        }
        return render(request=request, template_name='store/cart.html',context=context)