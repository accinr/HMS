from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('new/', views.patient_create, name='patient_create'),
    path('<int:pk>/', views.patient_detail, name='patient_detail'),

    # edit & delete
    path('<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('<int:pk>/delete/', views.patient_delete, name='patient_delete'),

    # medical records
    path('<int:patient_id>/records/', views.medicalrecord_list, name='medicalrecord_list'),
    path('<int:patient_id>/records/add/', views.medicalrecord_add, name='medicalrecord_add'),
    path('record/<int:pk>/', views.medicalrecord_detail, name='medicalrecord_detail'),
]
