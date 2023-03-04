from django.urls import path,include
from . import views


url_patterns=[
    path('',views.home,name='landingpage'),
    path('events',views.start,name='events'),]