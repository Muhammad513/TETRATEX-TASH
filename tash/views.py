from django.shortcuts import render
from .models import Tashish
# Create your views here.
def home(request):
    return render(request,'docs/dashboard.html')

def reestr(request):
    rees=Tashish.objects.all().order_by('-date').values('date','nak_num','transport__rusum','transport__tr_num','sofVazn','partiya__partiya',"ifloslik",'namlik','xisobiy','kond',"imzo")
    print(rees)

    context={'rees':rees}


    return render(request,'tashish/reestr.html',context)
