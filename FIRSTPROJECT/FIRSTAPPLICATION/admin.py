from django.contrib import admin
from .models import login_data,user_data,product_data

# Register your models here.
@admin.register(login_data)
class admin_user(admin.ModelAdmin):
    list_display = ['username','password']

@admin.register(user_data)
class admin_userdata(admin.ModelAdmin):
    list_display = ['id','Name','Contact','Address']

@admin.register(product_data)
class admin_productdata(admin.ModelAdmin):
    list_display = ['product_name','price','quantity']    
