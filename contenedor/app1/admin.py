from django.contrib import admin
from .models import AutorDb, FraseDb

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre", "fecha_de_nacimiento", "fecha_de_fallecimiento", "profesion", "nacionalidad"]
    list_display = ["nombre", "fecha_de_nacimiento"]
    
admin.site.register(AutorDb, AutorAdmin)

@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "autor_fk"]
    list_display = ["cita"]