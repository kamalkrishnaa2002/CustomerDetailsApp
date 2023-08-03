# storephone/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_form, name='store_form'),
     path('list/', views.store_list_view, name='store_list'),
    path('category/create/', views.create_category, name='create_category'),

]
