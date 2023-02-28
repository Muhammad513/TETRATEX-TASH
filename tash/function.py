import datetime
from django.db.models import Sum,Count,F,Q
def datenow(date):
    if date is None:
        x=datetime.datetime.now()
        date=x.strftime("%Y-%m-%d")
    else:
        date=date
    return date    

def partiya(obj,ptm,date):
    part=obj.objects.filter(tashish__ptm__name=ptm).annotate(
        sof=Sum('tashish__sofVazn'),
        birkunda=Sum('tashish__sofVazn',filter=Q(tashish__date=date)),
        fizik=Sum('tashish__kond'),
        koldiqs=(F('sofVazn')-Sum('tashish__sofVazn')),
        koldiqk=(F('kond')-Sum('tashish__kond')),
        
        )
    part=part.values(
        'partiya','bunt','nav__nav_name','snif',"sort",'sofVazn','xisobiy','kond','ifloslik','namlik','sof','fizik',"koldiqs","koldiqk","birkunda")
    return part