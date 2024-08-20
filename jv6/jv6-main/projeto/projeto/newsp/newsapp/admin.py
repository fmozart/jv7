from django.contrib import admin
from newsapp.models import Noticia

# Register your models here.
class Noticias(admin.ModelAdmin):
    list_display = ('data', 'titulo', 'imagem', 'paragrafo')
admin.site.register(Noticia, Noticias)

