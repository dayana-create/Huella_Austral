from django.contrib import admin
from .models import especie, ejemplar

@admin.register(especie)
class especieAdmin(admin.ModelAdmin):
    list_display= ('id','nombre')
    
@admin.register(ejemplar)
class ejemplarAdmin(admin.ModelAdmin):
    list_display=('id','nombre','especie','peso_kg','fecha_ingreso','liberado')
    list_filter= ('especie','liberado')
    
    



# Register your models here.
