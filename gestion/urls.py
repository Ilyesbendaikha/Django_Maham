from django.urls import path
from . import views
urlpatterns = [
    path('',views.loginpage,name="login"),
    path('register',views.registerpage,name="register"),
    path('home/',views.home,name="home"),
    path('logout/',views.logoutpage,name="logout"),
    path('addorder/',views.addorders,name="addorder"),
    path('update_order/<str:pk>/',views.update_order,name="update_order"),
    path('delete_order/<str:pk>/',views.delete_order,name="delete_order"),
    path('customers/',views.showcustomers,name="showcustomer"),
    path('Add Customer/',views.addcustomers,name="addcus"),
    path('update_customer/<str:pk>/',views.update_customer,name="update_customer"),
    path('Delete_customer/<str:pk>/',views.delete_customer,name="delete_customer"),
    path('Add_Offer/',views.addoffers,name="addoffer"),
    path('Offers/',views.showoffer,name="offers"),
    path('update_offer/<str:pk>/',views.update_offer,name="update_offer"),
    path('Delete_Offer/<str:pk>/',views.delete_offer,name="delete_offer"),
]
