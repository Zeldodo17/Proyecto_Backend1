from django.contrib import admin

from .models import (
    Usuario,
    Herramientas,
    Clasificacion
)

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Herramientas)
admin.site.register(Clasificacion)