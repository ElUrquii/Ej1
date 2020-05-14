from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=20)
    codigo=models.AutoField(primary_key=True)
    def str(self):
        return '{}'.format(self.nombre)

class Libro(models.Model):
    titulo=models.CharField(max_length=20)
    editorial=models.CharField(max_length=20)
    paginas=models.IntegerField
    codigo=models.AutoField(primary_key=True)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    def str(self):
        return '{}'.format(self.titulo)

class Ejemplar(models.Model):
    localizacion=models.CharField(max_length=20)
    codigo=models.AutoField(primary_key=True)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    def str(self):
        return '{}'.format(self.libro)

class Usuario(models.Model):
    nombre=models.CharField(max_length=20)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=20)
    codigo=models.AutoField(primary_key=True)
    ejemplares=models.ManyToManyField(Ejemplar)
    def str(self):
        return '{}'.format(self.nombre)
