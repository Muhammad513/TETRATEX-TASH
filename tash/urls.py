
from django.urls import path,include
from .views import formsfor,reestr,home

urlpatterns = [
    path('',home, name="home"),
    path('reestr/',reestr, name="reestr"),
    path('forms/',formsfor, name="formset"),

]
