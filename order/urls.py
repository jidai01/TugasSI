from django.urls import path
from . import views

urlpatterns = [
    # URL utama untuk laporan
    path('laporan/', views.laporan, name='laporan'),

    # URL untuk laporan pelanggan
    path('laporan/pelanggan/', views.laporan_pelanggan, name='laporan_pelanggan'),

    # URL untuk laporan kamar
    path('laporan/kamar/', views.laporan_kamar, name='laporan_kamar'),

    # URL untuk laporan pekerjaan
    path('laporan/pekerjaan/', views.laporan_pekerjaan, name='laporan_pekerjaan'),

    # URL untuk laporan tanggal
    path('laporan/tanggal/', views.laporan_tanggal, name='laporan_tanggal'),

    # URL untuk laporan pemesanan
    path('laporan/pemesanan/', views.laporan_pemesanan, name='laporan_pemesanan'),
]
