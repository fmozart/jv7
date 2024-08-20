from django.db import models
from shortuuid.django_fields import ShortUUIDField 
from django.utils.html import mark_safe


# Create your models here.

GENRE = (
    ("esporte", "Esporte"),
    ("politica", "Politica"),
    ("tecnologia", "Tecnologia"),
    ("social", "Social"),
)

class Noticia(models.Model):
    cid = ShortUUIDField(unique=True, length=5, max_length=10, alphabet="abcdef12345")
    titulo = models.CharField(max_length=50, default="Titulo")
    imagem = models.ImageField(upload_to="noticias/")
    paragrafo = models.TextField(null=True, blank=True)
    data = models.DateField(blank=True, null=True)
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Produtos"
    
    def imagem(self):
        return mark_safe('<img src ="%s" width="50"/>' % self.image.url)
    

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome