from django.urls import path
from .views import home, TrainDetailView, TrainCreateView, TrainUpdateView, TrainDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('create/', TrainCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete'),

]