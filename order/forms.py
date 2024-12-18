from django import forms
from .models import Pelanggan

class PelangganForm(forms.ModelForm):
    class Meta:
        model = Pelanggan
        fields = '__all__'

    tanggal_lahir = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Tanggal Lahir',
        required=True
    )
