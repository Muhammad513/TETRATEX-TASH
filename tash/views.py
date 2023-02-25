from django.shortcuts import render,redirect
from .models import Tashish,Transport,Partiya
from .forms import TashishForm,PartiyaForm
# Create your views here.
def home(request):
    user=request.user.profile
    context={'user':user}
    return render(request,'docs/dashboard.html',context)

def reestr(request):
    user=request.user.profile
    ptm=request.user.punkt
    
    rees=Tashish.objects.filter(ptm=ptm).values('date','nak_num','transport__rusum',
    'transport__tr_num','sofVazn','partiya__partiya',"ifloslik",'namlik','xisobiy',
    'kond',"imzo").order_by('-date')
    
    
    
    context={'rees':rees,'user':user}
    return render(request,'tashish/reestr.html',context)


def formsfor(request):
    user=request.user.profile
    ptm=request.user.punkt
    form=TashishForm(ptm)
    tash=Tashish.objects.filter(ptm=ptm).order_by('-id').values('date','nak_num','transport__rusum','transport__tr_num','sofVazn','partiya__partiya','ifloslik','namlik','xisobiy','kond','ptm__name')[0:10]
    if request.method == "POST":
        forms=TashishForm(ptm,request.POST)
        if forms.is_valid():
            formsets=forms.save(commit=False)
            formsets.ptm=ptm
            formsets.save()
            return redirect('formset')
    
    
    
    
    context={'user':user,'form':form,"tash":tash}
    return render(request,'forms/forms.html',context)

def xl_7(request):
    user=request.user.profile
    ptm=request.user.punkt
    form=PartiyaForm()
    part=Partiya.objects.filter(ptm=ptm).order_by('-id')
    if request.method == "POST":
        form=PartiyaForm(request.POST)
        if form.is_valid():
            formsets=form.save(commit=False)
            formsets.ptm=ptm
            formsets.save()
            return redirect('7xl')
    
    context={'user':user,"form":form,"part":part}
    return render(request,'forms/7xl.html',context)    