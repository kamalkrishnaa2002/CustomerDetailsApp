# storephone/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.store_form, name='store_form'),
    path('list/', views.store_list, name='store_list'),
    path('category/create/', views.create_category, name='create_category'),
]
