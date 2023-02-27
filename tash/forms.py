from .models import*
from django import forms
import datetime
from .views import*

x=datetime.datetime.now()
date=x.strftime("%Y-%m-%d")

class TashishForm(forms.ModelForm):
   
    class Meta:
        model=Tashish
        fields=('date','nak_num','transport','sofVazn','partiya','ifloslik','namlik')
        widgets={
            'nak_num':forms.TextInput(attrs={'type':'number'}),
            'sofVazn':forms.TextInput(attrs={'type':'number'}),
            'date':forms.TextInput(attrs={'type':'date','value':date}),
        }
    def __init__(self,ptm,*args,**kwargs):
        super (TashishForm,self ).__init__(*args,**kwargs) # populates the post
        self.fields['partiya'].queryset = Partiya.objects.filter(ptm=ptm)
        

class PartiyaForm(forms.ModelForm):
    class Meta:
        model=Partiya
        fields=('partiya','bunt','nav','sort','snif','sofVazn','xisobiy','kond')
        widgets={
                'sofVazn':forms.TextInput(attrs={'type':'number'}),
                'xisobiy':forms.TextInput(attrs={'type':'number'}),
                'kond':forms.TextInput(attrs={'type':'number'}),
                
                
            }
class TruckForm(forms.ModelForm):
    class Meta:
        model=Transport
        fields=('firma','rusum','tr_num')       

class FirmaForm(forms.ModelForm):
    class Meta:
        model=Firma
        fields=('name','narx')    

    

class TashishEdit(forms.ModelForm):
   
    class Meta:
        model=Tashish
        fields='__all__'
       