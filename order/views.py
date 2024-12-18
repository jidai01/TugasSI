from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pelanggan
from .forms import PelangganForm

class PelangganListView(ListView):
    model = Pelanggan
    template_name = 'order/pelanggan_list.html'

class PelangganCreateView(CreateView):
    model = Pelanggan
    form_class = PelangganForm
    template_name = 'order/pelanggan_form.html'
    success_url = reverse_lazy('pelanggan_list')

class PelangganUpdateView(UpdateView):
    model = Pelanggan
    form_class = PelangganForm
    template_name = 'order/pelanggan_form.html'
    success_url = reverse_lazy('pelanggan_list')

class PelangganDeleteView(DeleteView):
    model = Pelanggan
    template_name = 'order/pelanggan_confirm_delete.html'
    success_url = reverse_lazy('pelanggan_list')
