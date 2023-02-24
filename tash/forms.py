from .models import*
from django import forms
import datetime
from .views import*

x=datetime.datetime.now()
date=x.strftime("%Y-%m-%d")

class TashishForm(forms.ModelForm):
   
    class Meta:
        model=Tashish
        fields=['date','nak_num','transport','sofVazn','partiya','ifloslik','namlik']
        widgets={
            'nak_num':forms.TextInput(attrs={'type':'number'}),
            'sofVazn':forms.TextInput(attrs={'type':'number'}),
            'date':forms.TextInput(attrs={'type':'date','value':date}),
        }
    def __init__(self, user, *args, **kwargs):
            super(TashishForm, self).__init__(*args, **kwargs)
            self.fields['partiya'].queryset = Partiya.objects.filter(ptm=user)