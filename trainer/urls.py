from django.urls import path
from trainer import views

urlpatterns = [
    path('clients/', views.clientsList, name='clients-list'),
    path('clients/create', views.clientCreate, name='client-create'),
    path('client/<int:client_id>/', views.clientDetail, name='client-detail'),
    path('client/<int:client_id>/edit/', views.clientEdit, name='client-edit'),
    path('client/<int:client_id>/create/', views.clientTrainCreate, name='client-train-create'),
    path('client/<int:client_id>/<int:pk_train>/', views.clientTrain, name='client-train'),
    path('client/<int:client_id>/<int:pk_train>/update/', views.clientTrainUpdate, name='client-train-update'),
    path('new_date/', views.startPeriodCreate, name='new-date'),
]