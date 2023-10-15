from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
   
    
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('productdelete/<int:product_id>', views.productdelete, name='productdelete'),
    path('addnewproduct/', views.addnewproduct, name='addnewproduct'),
    path('productedit/<int:product_id>', views.productedit, name='productedit'),
]