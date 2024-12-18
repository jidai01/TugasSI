from django.urls import path
from .views import PelangganListView, PelangganCreateView, PelangganUpdateView, PelangganDeleteView

urlpatterns = [
    path('', PelangganListView.as_view(), name='pelanggan_list'),
    path('create/', PelangganCreateView.as_view(), name='pelanggan_create'),
    path('update/<str:pk>/', PelangganUpdateView.as_view(), name='pelanggan_update'),
    path('delete/<str:pk>/', PelangganDeleteView.as_view(), name='pelanggan_delete'),
]
