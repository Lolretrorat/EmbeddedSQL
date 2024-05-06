# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_address, name='add_address'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_practitioner/', views.add_practitioner, name='add_practitioner'),
    path('add_service/', views.add_service, name='add_service'),
    path('add_consultation/', views.add_consultation, name='add_consultation'),
    path('add_data/', views.add_address, name='add_data'),  
]
