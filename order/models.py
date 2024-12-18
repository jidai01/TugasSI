from django.db import models
from django.core.validators import MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError

# Model Pelanggan
class Pelanggan(models.Model):
    GENDER_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
    ]
    idPel = models.CharField(max_length=10, verbose_name='ID Pelanggan', null=False, unique=True, primary_key=True)
    namaDpn = models.CharField(max_length=50, verbose_name='Nama Depan', null=False)
    namaBlkng = models.CharField(max_length=50, verbose_name='Nama Belakang', null=False)
    jkPel = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='Jenis Kelamin')
    alamatPel = models.TextField(max_length=300, verbose_name='Alamat')
    pekerjaan = models.CharField(max_length=50, verbose_name='Pekerjaan')
    tglLahirPel = models.DateField(verbose_name='Tanggal Lahir')

    class Meta:
        verbose_name_plural = 'Data Pelanggan'
        ordering = ['idPel']

    def __str__(self):
        return f'{self.idPel} | {self.namaDpn} {self.namaBlkng}'

# Model NoTlpPel
class NoTlpPel(models.Model):
    idNoTlpPel = models.BigAutoField(verbose_name='ID Nomor Telepon', primary_key=True)
    idPel = models.ForeignKey(
        Pelanggan,
        on_delete=models.CASCADE,
        verbose_name='ID Pelanggan',
        related_name='nomor_telepon'
    )
    noTlpPel = models.CharField(
        max_length=20,
        verbose_name='Nomor Telepon',
        validators=[RegexValidator(r'^\d+$', 'Nomor telepon hanya boleh berisi angka.')]
    )

    class Meta:
        verbose_name_plural = 'Data Nomor Pelanggan'
        ordering = ['idNoTlpPel']

    def __str__(self):
        return f'{self.idNoTlpPel} | {self.idPel} > {self.noTlpPel}'

    def clean(self):
        if NoTlpPel.objects.filter(noTlpPel=self.noTlpPel).exclude(idNoTlpPel=self.idNoTlpPel).exists():
            raise ValidationError(f"Nomor telepon {self.noTlpPel} sudah terdaftar. Silakan gunakan nomor lain.")

# Model Kamar
class Kamar(models.Model):
    idKamar = models.CharField(max_length=10, verbose_name='ID Kamar', null=False, unique=True, primary_key=True)
    tipe = models.CharField(max_length=50, verbose_name='Tipe', null=False)
    kapasitas = models.PositiveIntegerField(verbose_name='Kapasitas', null=False)
    harga = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Harga',
        validators=[MinValueValidator(0)],
        null=False
    )

    class Meta:
        verbose_name_plural = 'Data Kamar'
        ordering = ['idKamar']

    def __str__(self):
        return f'{self.idKamar} | {self.tipe} > {self.kapasitas} > Rp. {self.harga}'

# Model Pesan
class Pesan(models.Model):
    idPesan = models.AutoField(verbose_name='ID Pesan', primary_key=True)
    idPel = models.ForeignKey(Pelanggan, verbose_name='ID Pelanggan', on_delete=models.CASCADE)
    jmlhKamar = models.PositiveIntegerField(verbose_name='Jumlah Kamar', null=False)

    class Meta:
        verbose_name_plural = 'Data Pesan Hotel'
        ordering = ['idPesan']

    def __str__(self):
        return f'{self.idPesan} | {self.idPel} > {self.jmlhKamar}'

# Model Detail Pesan
class DetailPesan(models.Model):
    STATUS_CHOICES = [
        ('A', 'APPROVED'),
        ('C', 'CANCELLED'),
        ('D', 'DONE'),
    ]
    idDetailPesan = models.AutoField(verbose_name='ID Detail Pemesanan', primary_key=True)
    idPesan = models.ForeignKey(Pesan, on_delete=models.CASCADE, verbose_name='ID Pemesanan')
    idKamar = models.ForeignKey(Kamar, on_delete=models.CASCADE, verbose_name='ID Kamar')
    tglCheckIn = models.DateField(verbose_name='Tanggal Check In')
    tglCheckOut = models.DateField(verbose_name='Tanggal Check Out')
    statusPesan = models.CharField(
        verbose_name='Status Pesan',
        max_length=1,
        choices=STATUS_CHOICES,
        default='A'
    )

    class Meta:
        verbose_name_plural = 'Data Detail Pesan'
        ordering = ['idDetailPesan']

    def __str__(self):
        return f'{self.idDetailPesan} | {self.idPesan} > {self.idKamar} > {self.tglCheckIn} - {self.tglCheckOut} > {self.statusPesan}'

    def clean(self):
        # Validasi untuk mencegah pemesanan kamar pada tanggal yang sudah dipesan
        overlapping_bookings = DetailPesan.objects.filter(
            idKamar=self.idKamar,
            tglCheckOut__gte=self.tglCheckIn,
            tglCheckIn__lte=self.tglCheckOut,
        ).exclude(idDetailPesan=self.idDetailPesan)
        if overlapping_bookings.exists():
            raise ValidationError("Kamar ini sudah dipesan dalam rentang tanggal tersebut.")

        # Validasi jumlah kamar yang dipesan tidak melebihi jmlhKamar pada Pesan
        total_booked_rooms = DetailPesan.objects.filter(idPesan=self.idPesan).count()
        max_rooms = self.idPesan.jmlhKamar

        if total_booked_rooms >= max_rooms:
            raise ValidationError(
                f"Jumlah kamar yang dipesan untuk ID Pesan {self.idPesan.idPesan} sudah mencapai batas maksimal ({max_rooms})."
            )

    def save(self, *args, **kwargs):
        # Jalankan validasi sebelum menyimpan
        self.full_clean()
        super().save(*args, **kwargs)