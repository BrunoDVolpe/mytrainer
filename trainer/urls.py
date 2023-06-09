from django.urls import path
from trainer import views

urlpatterns = [
    path('clients/', views.clientsList, name='clients-list'),
    path('client/<int:id>/', views.clientDetail, name='client-detail'),
    path('client/<int:id>/<int:train>/', views.clientDetail, name='client-detail'),
]