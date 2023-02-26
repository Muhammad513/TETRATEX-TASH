from django.urls import path,include
from .views import*
urlpatterns = [
    path('',loginPage,name='login'),
    path('',logout,name='logout')
]
