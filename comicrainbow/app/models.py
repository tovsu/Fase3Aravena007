from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comic(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    fecha_lanzamiento = models.DateField()
    imagen = models.ImageField(upload_to="comics", null=True)

    def __str__(self):
        return self.nombre

opciones_consultas = [
        [0, "consulta"],
        [1, "reclamo"],
        [2, "sugernecia"],
        [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
