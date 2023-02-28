from django.shortcuts import render,redirect
from .models import Tashish,Transport,Partiya,DisplaySetting,Firma,Punkt
from .forms import TashishForm,PartiyaForm,TruckForm,FirmaForm,TashishEdit
# Create your views here.++
from .decarators import check_user_able_to_see_page
from .function import datenow,partiya
from django.db.models import Sum,Count
from django.db.models import  F,IntegerField,FloatField






def home(request):
    user=request.user.profile
    context={'user':user}
    return render(request,'docs/dashboard.html',context)


@check_user_able_to_see_page("PTM")
def reestr(request):
    user=request.user.profile
    ptm=request.user.punkt
    
    rees=Tashish.objects.filter(ptm=ptm).values('date','nak_num','transport__rusum',
    'transport__tr_num','sofVazn','partiya__partiya',"ifloslik",'namlik','xisobiy',
    'kond',"imzo").order_by('-date')
    
    
    
    context={'rees':rees,'user':user}
    return render(request,'tashish/reestr.html',context)

@check_user_able_to_see_page("PTM")
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


def truck(request):
    form=TruckForm()
    user=request.user.profile
    truck=Transport.objects.values('firma__name','rusum','tr_num','user__first_name').order_by('-id')[0:15]
    if request.method == "POST":
        form=TruckForm(request.POST)
        if form.is_valid():
            forms=form.save(commit=False)
            forms.user=request.user
            forms.save()
            return redirect('truck')
    
    context={'user':user,"form":form,"truck":truck}
    return render(request,'forms/truck.html',context)    

def firma(request):
    form=FirmaForm()
    user=request.user.profile
    firma=Firma.objects.order_by('-id')[0:15].values('name','user__first_name','narx')
    if request.method == "POST":
        form=FirmaForm(request.POST)
        if form.is_valid():
            forms=form.save(commit=False)
            forms.user=request.user
            forms.save()
            return redirect('firma')
    
    context={'user':user,"form":form,"firma":firma}
    return render(request,'forms/firma.html',context)    


def error_404_view(request,exception):
    user=request.user.profile
    return render(request, 'docs/404.html',{'user':user})


@check_user_able_to_see_page("ADMINS") 
def infores(request):
    date=request.POST.get("date")
    date=datenow(date)
    user=request.user.profile

    tash=Tashish.objects.filter(date=date,imzo=False).values('date','nak_num','transport__tr_num','sofVazn','partiya__partiya','ifloslik','namlik','xisobiy','kond','imzo','partiya__nav__nav_name','partiya__sort','partiya__snif',"ptm__name",'id')
    
    context={"tash":tash,'user':user,"date":date}
    return render(request,'info/info.html',context)


@check_user_able_to_see_page("ADMINS")    
def update(request,pk):
    user=request.user.profile
    tash=Tashish.objects.get(id=pk)
    form=TashishEdit(instance=tash)
    
    if request.method == "POST":
        form=TashishEdit(request.POST,instance=tash)
        if form.is_valid():
            form.save()
            return redirect('info')
    
    context={'user':user,'form':form,"tash":tash}
    return render(request,'imzo/imzo.html',context)
    
@check_user_able_to_see_page("ADMINS")
def tasdiq(request):
    date=request.POST.get("date")
    date=datenow(date)
    user=request.user.profile

    tash=Tashish.objects.filter(date=date,imzo=True).values('date','nak_num','transport__tr_num','sofVazn','partiya__partiya','ifloslik','namlik','xisobiy','kond','imzo','partiya__nav__nav_name','partiya__sort','partiya__snif',"ptm__name",'id')
    
    context={"tash":tash,'user':user,"date":date}
    return render(request,'info/reestr-tasdiq.html',context)


def ptm7xl(request):
    user=request.user.profile
    date=request.POST.get("date")
    date=datenow(date)
    ptm=request.POST.get('ptm')
    choices=Punkt.objects.all().values('name')
    part=partiya(Partiya,ptm,date)
    
    context={'user':user,"date":date,"user":user,'part':part,"choices":choices,"ptm":ptm}
    return render(request,'ptm/ptm7xl.html',context)

