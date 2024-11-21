from django.db import models
import datetime
import os

def filename(request, filename):
     timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
     base_filename = "%s%s"%(timestamp,filename)
     return os.path.join('uploads/', base_filename)
 
 
class category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=filename,null=True,blank=True)
    description = models.CharField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending = models.BooleanField(default=False)
    
    
   
    

   

    def __str__(self):
        return self.name
class products(models.Model):
    Category=models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=False)
    vendar = models.CharField(max_length=100,null=False)
    product_image = models.ImageField(upload_to=filename,null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)
    description = models.CharField(max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0-show,1-Hidden") 
    trending = models.BooleanField(default=False) 
    
    
    
    def __str__(self):
        return self.name

# Create your models here.
