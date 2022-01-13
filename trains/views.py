from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import TrainCreateForm
from .models import Train


def home(request):
    trains_list = Train.objects.all()
    paginator = Paginator(trains_list, 5)
    page = request.GET.get('page')
    trains_list = paginator.get_page(page)
    return render(request, 'trains/home.html', {'trains_list': trains_list})


class TrainCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Train
    form_class = TrainCreateForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Train added success'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    context_object_name = 'train'
    template_name = 'trains/detail.html'


class TrainUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Train
    form_class = TrainCreateForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Train updated success'


class TrainDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('train:home')
    success_message = 'Train deleted success'




