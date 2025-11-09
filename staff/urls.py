from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('<int:pk>/', views.doctor_detail, name='doctor_detail'),

    # create, edit, delete
    path('new/', views.doctor_create, name='doctor_create'),
    path('<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
]
