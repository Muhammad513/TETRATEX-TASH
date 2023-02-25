from django.contrib import admin
from .models import Punkt,Partiya,Tashish,Firma,Transport
# Register your models here.
class PunktAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'bux')

class PartiyaAdmin(admin.ModelAdmin):
    list_display = ('id','ptm','partiya', 'bunt',"nav","sort",'snif',"sofVazn",'ifloslik',"xisobiy",'namlik','kond')
    

class TashishAdmin(admin.ModelAdmin):
    
    @admin.display(description="Tashish")
    def admin_date(self,obj):
        return obj.date.strftime('%d-%m-%Y')
    
    
    list_display = ('id','admin_date', 'nak_num',"transport","sofVazn",'partiya',"ifloslik",'namlik',"xisobiy",'kond')


class FirmaAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class TransportAdmin(admin.ModelAdmin):
    list_display = ('id','firma', 'rusum',"tr_num",)








admin.site.register(Punkt,PunktAdmin) 
admin.site.register(Partiya,PartiyaAdmin)    
admin.site.register(Tashish,TashishAdmin)
admin.site.register(Transport,TransportAdmin)
admin.site.register(Firma,FirmaAdmin)    






 