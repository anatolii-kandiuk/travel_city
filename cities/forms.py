from django import forms
from .models import City


class CityCreateForm(forms.ModelForm):
    name = forms.CharField(label='City',
                           widget=forms.TextInput(
                                        attrs={'class': 'form-control',
                                               'placeholder': 'Type city name'}))

    class Meta(object):
        model = City
        fields = ('name', )

