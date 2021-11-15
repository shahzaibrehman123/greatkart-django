from django.contrib import admin
from django.db import models
from .models import product




class productAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name' ,)}

admin.site.register(product, productAdmin)

# Register your models here.
