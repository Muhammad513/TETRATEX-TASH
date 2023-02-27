
from django.urls import path,include
from .views import formsfor,reestr,home,xl_7,truck,firma,infores,update

urlpatterns = [
    path('',home, name="home"),
    path('reestr/',reestr, name="reestr"),
    path('forms/',formsfor, name="formset"),
    path('shakl7/',xl_7, name="7xl"),
    path('transport/',truck, name="truck"),
    path('firma/',firma, name="firma"),
    path('info/',infores, name="info"),
    path('imzo/<str:pk>/',update, name="imzo"),

]
