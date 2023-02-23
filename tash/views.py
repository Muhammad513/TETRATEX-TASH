from django.shortcuts import render
from .models import Tashish
# Create your views here.
def home(request):
    user=request.user.profile
    context={'user':user}
    return render(request,'docs/dashboard.html',context)

def reestr(request):
    s=request.user.punkt.id
    print(s)


    rees=Tashish.objects.filter.order_by('-date').values('date','nak_num','transport__rusum','transport__tr_num','sofVazn','partiya__partiya',"ifloslik",'namlik','xisobiy','kond',"imzo")
    user=request.user.profile

    context={'rees':rees,'user':user}


    return render(request,'tashish/reestr.html',context)
