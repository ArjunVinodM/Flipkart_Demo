from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def product_detail(request):
    return render(request,'product-detail.html')

def add_to_cart(request):
    return render(request,'add-to-cart.html')

def buy_now(request):
    return render(request,'buy-now.html')

def checkout(request):
    return render(request,'checkout.html')

def login(request):
    return render(request,'login.html')

def customer_registration(request):
    return render(request,'customer-registration.html')

def profile(request):
    return render(request,'profile.html')

def address(request):
    return render(request,'address.html')

def order(request):
    return render(request,'order.html')

def change_password(request):
    return render(request,'change-password.html')

def mobile(request):
    return render(request,'mobile.html')

def laptop(request):
    return render(request,'laptop.html')