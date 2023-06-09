from django.urls import path
from trainer import views

urlpatterns = [
    path('clients/', views.clientsList, name='clients-list'),
    path('client/<int:id>/', views.clientDetail, name='client-detail'),
    path('client/<int:id>/<int:pk_train>/', views.clientDetail, name='client-detail'),
    path('client/<int:id>/<int:pk_train>/update/', views.clientTrainUpdate, name='client-train-update'),
]