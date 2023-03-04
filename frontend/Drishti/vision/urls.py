from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('camera',views.camera,name='camera'),
    path('start',views.start,name='start'),]