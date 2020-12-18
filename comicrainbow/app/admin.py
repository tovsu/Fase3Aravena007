from django.contrib import admin
from .models import Editorial, Comic, Contacto
# Register your models here.

class ComicAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "editorial"]


admin.site.register(Editorial)
admin.site.register(Comic, ComicAdmin)
admin.site.register(Contacto)