from django.db import models
from django.contrib.auth.models import User
from PIL import Image



class Profile(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    pic=models.ImageField(upload_to='img',blank=True,null=True,default='default/default.jpg')
    pic_thumbnail=models.ImageField(upload_to='img',blank=True,null=True,default='default/thumbnail.jpg')


    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img=Image.open(self.pic.path)

        if img.height>150 and img.width>150:
            output_size=(50,50)
            img.thumbnail(output_size)
            img.save(self.pic_thumbnail.path)     