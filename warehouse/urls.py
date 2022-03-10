from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('customer_search/', views.customer_search_view, name='customer_search'),
    path('product_search/', views.product_search_view, name='product_search'),
    path('customer/', views.customer_view, name='customer'),
    path('options/', views.options_view, name='options'),
    path('warehouse/', views.warehouse_view, name='warehouse'),
    path('warehouse_export/', views.export_warehouse_details, name='export_details'),
    path('customer_export/', views.export_customer, name='export_customer'),
    
]