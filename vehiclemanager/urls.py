from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.add_vehicle, name='add_vehicle'),
    path('edit/<int:vehicle_id>/', views.edit_vehicle, name='edit_vehicle'),
    path('delete/<int:vehicle_id>/', views.delete_vehicle, name='delete_vehicle'),
]
