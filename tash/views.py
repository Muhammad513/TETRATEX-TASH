from django.shortcuts import render
from .models import Tashish,Transport,Partiya
from .forms import TashishForm
# Create your views here.
def home(request):
    user=request.user.profile
    context={'user':user}
    return render(request,'docs/dashboard.html',context)

def reestr(request):
    user=request.user.profile

    rees=Tashish.objects.filter().values('date','nak_num','transport__rusum',
    'transport__tr_num','sofVazn','partiya__partiya',"ifloslik",'namlik','xisobiy',
    'kond',"imzo").order_by('-date')
    
    
    
    context={'rees':rees,'user':user}
    return render(request,'tashish/reestr.html',context)


def formsfor(request):
    user=request.user.profile
    ptm=request.user.punkt.id
    partiya=Partiya.objects.filter(ptm=ptm)
    tr_list=Transport.objects.all()
    form=TashishForm(request.POST)
    tash=Tashish.objects.filter(ptm=ptm).order_by('-date').values('date','nak_num','transport__rusum','transport__tr_num','sofVazn','partiya__partiya','ifloslik','namlik','xisobiy','kond','ptm__name')[0:10]
    context={'user':user,'form':form,"tr_list":tr_list,"partiya":partiya,"tash":tash}
    return render(request,'forms/forms.html',context)