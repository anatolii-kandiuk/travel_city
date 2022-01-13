from django.urls import path
from .views import home, CityDetailView, CityCreateView, CityUpdateView, CityDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('create/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),

]