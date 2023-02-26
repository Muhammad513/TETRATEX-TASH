from django.db import models
from django.contrib.auth.models import User
from .choices import*

class Punkt(models.Model):
    name=models.CharField(max_length=20)
    bux=models.OneToOneField(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Пахта тозалаш масканлари"    


    def __str__(self):
        return str(self.name)


class Partiya(models.Model):
    ptm=models.ForeignKey('Punkt',on_delete=models.SET_NULL,null=True)
    partiya=models.CharField(max_length=7,verbose_name='ПАРТИЯ РАКАМИ')
    bunt=models.CharField(max_length=20,verbose_name='Жой РАКАМИ')
    nav=models.ForeignKey("PaxtaNavi",on_delete=models.SET_NULL,verbose_name='Селекцион Нав',help_text='Анд-35,Анд-36,Шарк',null=True)
    sort=models.CharField(max_length=1,verbose_name='Пахтанинг Сорти',choices=sort)
    snif=models.CharField(max_length=1,verbose_name='Пахтанинг снифи',choices=snif)
    sofVazn=models.FloatField(verbose_name='Соф вазни')
    xisobiy=models.FloatField(verbose_name='Хисобий вазни')
    kond=models.FloatField(verbose_name='Кондицион вазни')
    ifloslik=models.FloatField(blank=True,verbose_name='Ифлослиги')
    namlik=models.FloatField(blank=True,verbose_name='Намлиги')
    

    def save(self,*args,**kwargs):
        self.ifloslik=round(100-((self.xisobiy*98)/self.sofVazn),1)
        self.namlik=round(((self.xisobiy*109)/self.kond)-100,1)
        super().save(*args,**kwargs)


    class Meta:
        verbose_name_plural = "Партиялар очиш"    

    def __str__(self):
        return str(self.partiya)    

class Firma(models.Model):
    name=models.CharField(max_length=20,verbose_name='Фирма номи',help_text="М: AGRMOMAX MCHJ")
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    narx=models.FloatField(null=True)
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Ташувчи Фирмалар"    

class Transport(models.Model):
    firma=models.ForeignKey('Firma',on_delete=models.PROTECT,verbose_name='Фирма')
    rusum=models.CharField(max_length=20,verbose_name='Транспорт маркаси')
    tr_num=models.CharField(max_length=20,verbose_name='Транспорт раками')
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name_plural = "Т/Р руйхатдан утказиш"
    
    def __str__(self):
        return str(self.tr_num)



class Tashish(models.Model):
    ptm=models.ForeignKey('Punkt',on_delete=models.SET_NULL,null=True,related_name='ptm')
    date=models.DateField()
    nak_num=models.CharField(max_length=20,verbose_name='Накладной раками')
    transport=models.ForeignKey('Transport',on_delete=models.SET_NULL,verbose_name='Транспортни танланг',null=True)
    sofVazn=models.FloatField(verbose_name='Соф Вазни')
    partiya=models.ForeignKey("Partiya",on_delete=models.SET_NULL,verbose_name='Партия раками',null=True)
    ifloslik=models.FloatField(verbose_name='Ифлослиги')
    namlik=models.FloatField(verbose_name='Намлиги')
    xisobiy=models.FloatField(blank=True,verbose_name='Хисобий Вазни')
    kond=models.FloatField(blank=True,verbose_name='Кондицион Вазни')
    imzo=models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "ПАХТАНИ ТАШИШ"
    
    def save(self,*args,**kwargs):
        self.xisobiy=round((self.sofVazn*((100-self.ifloslik)/98)),1)
        self.kond=round((self.sofVazn*((100-self.ifloslik)/98))*(109/(100+self.namlik)),1)
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.date)


class PaxtaNavi(models.Model):
    nav_name=models.CharField(max_length=20)


    class Meta:
        verbose_name_plural = "Пахта Навлари"
    
    def __str__(self):
        return str(self.nav_name)        
    

class DisplaySetting(models.Model):
    name=models.CharField(max_length=20,null=True)
    display=models.BooleanField(default=False,verbose_name='Дисплейни учириш')    

    def __str__(self):
        return str(self.name)    
    
    class Meta:
        verbose_name_plural = "DISPLAY СОЗЛАМАЛАРИ"