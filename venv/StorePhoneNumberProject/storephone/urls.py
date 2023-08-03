# storephone/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_form, name='store_form'),
    path('list/', views.store_list_view, name='store_list'),
    path('category/create/', views.create_category, name='create_category'),
    path('update_button_clicked/<int:store_id>/', views.update_button_clicked, name='update_button_clicked'),
]
