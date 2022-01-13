from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import CityCreateForm
from .models import City


def home(request):
    list_cities = City.objects.all()
    paginator = Paginator(list_cities, 5)
    page = request.GET.get('page')
    list_cities = paginator.get_page(page)
    return render(request, 'cities/home.html', {'cities_list': list_cities})


class CityDetailView(DetailView):
    queryset = City.objects.all()
    context_object_name = 'city'
    template_name = 'cities/detail.html'


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = City
    form_class = CityCreateForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('city:home')
    success_message = 'City added success'


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = City
    form_class = CityCreateForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('city:home')
    success_message = 'City updated success'


class CityDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('city:home')
    success_message = 'City deleted success'




