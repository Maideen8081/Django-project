from django.contrib import admin
from . models import  *

class productAdmin(admin.ModelAdmin):
    list_display=('name','image','description')
    
    
admin.site.register(category,productAdmin)
admin.site.register(products)

# Register your models here.
