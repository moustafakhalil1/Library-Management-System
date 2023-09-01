from distutils.command.install_egg_info import to_filename
from pyexpat import model
from django.db import models
# Create your models here.
class category(models.Model):
   name=models.CharField(max_length=50)
  #عشان اخلي الفئه تظهر في قاعده البيانات بالاسم اللي انا بديهولها لازم اعمل الفانكشن دي 
   def __str__(self):
       return  self.name


class books(models.Model):
     book_status=[
      ('available','available'),
      ('rental','rental'),
      ('sold','sold'),
     ]
  

     Title=models.CharField(max_length=250)
     author=models.CharField(max_length=250,null=True,blank=True)
     photo_book=models.ImageField(upload_to='photo',null=True,blank=True)
     photo_author=models.ImageField(upload_to='photo',null=True,blank=True)
     pages=models.IntegerField(null=True,blank=True)
     price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
     rental_day_pric=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
     rental_priod=models.IntegerField(null=True,blank=True)
     total_pric=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
     active=models.BooleanField(default=True)
     status=models.CharField(max_length=50,choices=book_status,null=True,blank=True)
     category=models.ForeignKey(category,on_delete=models.PROTECT,null=True,blank=True)
     
     #فانكشن عشان اسم الكتاب  
     def __str__(self):
       return  self.Title
class earn(models.Model):
   total_price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)

