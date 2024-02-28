from django import forms

from movieapp.models import Movies


class modelform(forms.ModelForm):
    class Meta:
        model=Movies
        fields=["name","desc","year","imag"]