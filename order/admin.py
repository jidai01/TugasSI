from django.contrib import admin
from .models import Pelanggan, Kamar, Pesan, DetailPesan,NoTlpPel
# Register your models here.
admin.site.register(Pelanggan)
admin.site.register(Kamar)
admin.site.register(Pesan)
admin.site.register(DetailPesan)
admin.site.register(NoTlpPel)