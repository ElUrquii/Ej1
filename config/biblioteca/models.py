from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.AutoField(primary_key = True)
    def __str__(self):
        return str(self.nombre)

class Libro(models.Model):
    codigo = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 30)
    editorial = models.CharField(max_length = 30)
    paginas = models.IntegerField(default = '0')
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.titulo)

class Ejemplar(models.Model):
    codigo = models.AutoField(primary_key = True)
    localizacion = models.CharField(max_length = 30)
    libro = models.ForeignKey(Libro, on_delete = models.CASCADE)

    def __str__(self):
        return str('Ejemplar ' + str(self.codigo) + ' de ' + str(self.libro))

class Usuario(models.Model):
    telefono = models.IntegerField()
    codigo = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length = 30)
    ejemplar = models.ManyToManyField(Ejemplar)
    def __str__(self):
        return str(self.nombre)
