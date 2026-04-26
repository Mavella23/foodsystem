from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/customer/', views.customer_dashboard, name='customer_dashboard'),
    path('dashboard/vendor/', views.vendor_dashboard, name='vendor_dashboard'),
    path('dashboard/delivery/', views.delivery_dashboard, name='delivery_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
]
