from django.shortcuts import render

def home(request):
    context = {
    "products": [
        {"name": "apple"},
        {"name": "banana"},
        {"name": "cherry"}
    ]
    }
    return render(request, 'home/home.html',context)

from django.http import JsonResponse

def product(request):
    products = [
        {"name": "apple"},
        {"name": "banana"},
        {"name": "cherry"}
    ]
    return JsonResponse({"products": products})
