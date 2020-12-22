from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    HomeView,
    add_to_cart,
    OrderSummeryView,
    remove_from_cart
)



app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('checkout/', checkout , name='checkout'),
    path('order-summary/', OrderSummeryView.as_view() , name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view() , name='product'),
    path('add-to-cart/<slug>/', add_to_cart , name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart , name='remove-from-cart')
]