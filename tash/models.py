from django.db import models
from django.contrib.auth.models import User


class Punkt(models.Model):
    name=models.CharField(max_length=20)
    bux=models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)


class Partiya(models.Model):
    xosil=models.CharField(max_length=4)
    partiya=models.CharField(max_length=7)
    bunt=models.CharField(max_length=20)
    nav=models.CharField(max_length=30)
    sort=models.CharField(max_length=1)
    snif=models.CharField(max_length=1)
    sofVazn=models.FloatField()
    xisobiy=models.FloatField()
    kond=models.FloatField()
    ifloslik=models.FloatField(blank=True)
    namlik=models.FloatField(blank=True)


    def save(self,*args,**kwargs):
        self.ifloslik=round(100-((self.xisobiy*98)/self.sofVazn),1)
        self.namlik=round(((self.xisobiy*109)/self.kond)-100,1)
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.partiya)    

class Firma(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class Transport(models.Model):
    firma=models.ForeignKey('Firma',on_delete=models.CASCADE)
    rusum=models.CharField(max_length=20)
    tr_num=models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.tr_num)



class Tashish(models.Model):
    date=models.DateField(auto_now=True)
    nak_num=models.CharField(max_length=20)
    transport=models.ForeignKey('Transport',on_delete=models.CASCADE)
    sofVazn=models.FloatField()
    partiya=models.ForeignKey("Partiya",on_delete=models.CASCADE)
    ifloslik=models.FloatField()
    namlik=models.FloatField()
    xisobiy=models.FloatField(blank=True)
    kond=models.FloatField(blank=True)
    

    
    def save(self,*args,**kwargs):
        self.xisobiy=round((self.sofVazn*((100-self.ifloslik)/98)),1)
        self.kond=round((self.sofVazn*((100-self.ifloslik)/98))*(109/(100+self.namlik)),1)
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.date)