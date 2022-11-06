from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('product-detail/',views.product_detail, name='product-detail'),
    path('cart/',views.add_to_cart, name='add-to-cart'),
    path('buy/',views.buy_now, name='buy-now'),
    path('checkout/',views.checkout, name='checkout'),
    path('login/',views.login, name='login'),
    path('customer-registration/',views.customer_registration, name='customer-registration'),
    path('profile/',views.profile, name='profile'),
    path('address/',views.address, name='address'),
    path('order/',views.order, name='order'),
    path('change-password/',views.change_password, name='change-password'),
    path('mobile/',views.mobile, name='mobile'),
    path('laptop/', views.laptop, name='laptop'),







]