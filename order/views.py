from django.shortcuts import render
from django.http import HttpResponse
from .models import Pelanggan, Kamar, Pesan, DetailPesan
from django.db.models import Count, Sum

# Laporan Utama
def laporan(request):
    return render(request, 'laporan.html')

# Laporan Pelanggan
def laporan_pelanggan(request):
    # Menghitung jumlah kamar yang dipesan setiap pelanggan dan mengurutkannya
    pelanggan = Pelanggan.objects.annotate(
        total_kamar=Sum('pesan__jmlhKamar')
    ).order_by('-total_kamar')  # Urutkan berdasarkan total kamar yang dipesan (terbesar ke terkecil)

    # Kirim data pelanggan ke template
    return render(request, 'laporan_pelanggan.html', {'pelanggan': pelanggan})
# Laporan Kamar
def kamar_terbanyak_dipesan():
    # Menghitung jumlah pesanan per tipe kamar
    kamar_dipesan = Kamar.objects.annotate(
        jumlah_dipesan=Count('detailpesan')
    ).order_by('-jumlah_dipesan')  # Urutkan dari yang terbanyak

    # Membuat laporan
    laporan = []
    for kamar in kamar_dipesan:
        laporan.append({
            'id_kamar': kamar.idKamar,
            'tipe': kamar.tipe,
            'kapasitas': kamar.kapasitas,
            'harga': kamar.harga,
            'jumlah_dipesan': kamar.jumlah_dipesan
        })
    
    return laporan

def laporan_kamar(request):
    # Mendapatkan data laporan kamar yang terbanyak dipesan
    laporan = kamar_terbanyak_dipesan()
    
    # Render tampilan laporan kamar
    return render(request, 'laporan_kamar.html', {'laporan': laporan})
# Laporan Pekerjaan
def laporan_pelanggan_pekerjaan():
    # Menghitung jumlah pesanan berdasarkan pekerjaan pelanggan
    pelanggan_terbanyak_pesanan = Pelanggan.objects.annotate(
        jumlah_pesanan=Count('pesan')  # Menghitung jumlah pesanan berdasarkan relasi ke model Pesan
    ).order_by('-jumlah_pesanan')  # Mengurutkan dari yang terbanyak

    # Membuat laporan pelanggan
    laporan = []
    for pelanggan in pelanggan_terbanyak_pesanan:
        laporan.append({
            'id_pelanggan': pelanggan.idPel,
            'nama': f'{pelanggan.namaDpn} {pelanggan.namaBlkng}',
            'pekerjaan': pelanggan.pekerjaan,
            'jumlah_pesanan': pelanggan.jumlah_pesanan
        })

    return laporan

def laporan_pekerjaan(request):
    # Mendapatkan data laporan pelanggan berdasarkan pekerjaan dan jumlah pesanan
    laporan = laporan_pelanggan_pekerjaan()
    
    # Render halaman laporan pelanggan
    return render(request, 'laporan_pekerjaan.html', {'laporan': laporan})

# Laporan Tanggal
def laporan_tanggal(request):
    # Menghitung jumlah pemesanan berdasarkan tanggal check-in
    pemesanan_per_tanggal = DetailPesan.objects.values('tglCheckIn') \
        .annotate(jumlah_pemesanan=Count('idDetailPesan')) \
        .order_by('-jumlah_pemesanan')  # Urutkan dari yang terbanyak ke terkecil

    # Mengirimkan data ke template
    return render(request, 'laporan_tanggal.html', {'pemesanan_per_tanggal': pemesanan_per_tanggal})

# Laporan Pemesanan
def laporan_pemesanan(request):
    # Ambil semua data pemesanan beserta detailnya
    pesan_list = Pesan.objects.all()
    
    # Menampilkan data pemesanan dalam format yang diinginkan
    context = {
        'pesan_list': pesan_list,
    }
    
    return render(request, 'laporan_pemesanan.html', context)