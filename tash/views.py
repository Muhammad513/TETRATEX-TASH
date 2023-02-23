from django.shortcuts import render
from .models import Tashish
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

    form=TashishForm(request.POST)
    context={'user':user,'form':form}
    return render(request,'forms/forms.html',context)