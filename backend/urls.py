from django.urls import path
from backend import views

urlpatterns = [
    path('index/', views.index, name="index"),    #index
    path('done/<int:dataid>/', views.done, name="done"),
    path('addadmin/', views.addadmin, name="addadmin"),
    path('register/', views.register, name="register"),
    path('displaya/', views.displaya, name="displaya"),
    path('editadmin/<int:dataid>/', views.editadmin, name="editadmin"),
    path('updateadmin/<int:dataid>/', views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),

    path('instrumentone/', views.instrumentone, name="instrumentone"),
    path('addinstrument/', views.addinstrument, name="addinstrument"),
    path('instrumenttwo/', views.instrumenttwo, name="instrumenttwo"),
    path('editinst/<int:dataid>/', views.editinst, name="editinst"),
    path('updateinst/<int:dataid>/', views.updateinst, name="updateinst"),
    path('deleteinst/<int:dataid>/', views.deleteinst, name="deleteinst"),

    path('productone/', views.productone, name="productone"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('producttwo/', views.producttwo, name="producttwo"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),

    path('', views.logina, name="logina"),
    path('mainadmin/', views.mainlogin, name="mainadmin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

    path('reviewmess/', views.reviewmess, name="reviewmess"),
    path('reviewdelete/<int:dataid>/', views.reviewdelete, name="reviewdelete")

]