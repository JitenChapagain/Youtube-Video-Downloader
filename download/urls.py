from django.urls import path
from .views import *

urlpattern = [
    path('',index,name='index')
]