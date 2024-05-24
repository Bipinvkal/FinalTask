from django import forms
from .models import Addmovie

class movForm(forms.ModelForm):
    class Meta:
        model=Addmovie
        fields=['movie_title','poster','category','discription','relese_date','rate','actor']
        widgets={
            'movie_title':forms.TextInput(attrs={'class':'form-control'}),
            'discription': forms.TextInput(attrs={'class': 'form-control'}),
            'poster':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'relese_date': forms.DateInput(attrs={'class': 'form-control'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'actor': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }