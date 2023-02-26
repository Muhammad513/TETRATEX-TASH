
from django.urls import path,include
from .views import formsfor,reestr,home,xl_7,truck,firma

urlpatterns = [
    path('',home, name="home"),
    path('reestr/',reestr, name="reestr"),
    path('forms/',formsfor, name="formset"),
    path('shakl7/',xl_7, name="7xl"),
    path('transport/',truck, name="truck"),
    path('firma/',firma, name="firma"),

]
