from .models import Tashish
from django import forms



class TashishForm(forms.ModelForm):
    class Meta:
        model=Tashish
        fields=['nak_num','transport','sofVazn','partiya','ifloslik','namlik']
        widgets={
            'nak_num':forms.TextInput(attrs={'type':'number'}),
            'sofVazn':forms.TextInput(attrs={'type':'number'}),
            
            
        }