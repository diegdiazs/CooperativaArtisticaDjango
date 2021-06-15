from django.db import models

# Create your models here.

class Categoria(models.Model):

  idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de categoría')
  nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de la categpria')

def __str__(self):
       return self.nombreCategoria



class obradearte(models.Model):

 nombreobra = models.CharField(max_length=20, primary_key=True , verbose_name='nombreobra')
 dimenciones = models.CharField(max_length=15,blank=True ,verbose_name='dimenciones')
 añocreacion = models.CharField(max_length=6,null=True, blank=True, verbose_name='año de creacion')
 categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

def __str__(self):
 return self.nombreobra




