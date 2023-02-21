from frontend import views
from django.urls import path


urlpatterns=[
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('inst/<itemcatg>', views.inst, name="inst"),
    path('single/<int:dataid>', views.single, name="single"),
    path('loginc/', views.loginc, name="loginc"),
    path('deal/', views.deal, name="deal"),
    path('customer/', views.customer, name="customer"),
    path('customerl/', views.customerl, name="customerl"),
    path('customerd/', views.customerd, name="customerd"),
    path('reviewc/', views.reviewc, name="reviewc"),
    path('delivery/<int:dataid>', views.delivery, name="delivery")
]