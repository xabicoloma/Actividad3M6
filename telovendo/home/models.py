from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):


  username = models.CharField(max_length=50, null=False, unique=True)
  nombre = models.CharField(max_length=50,  null=True)
  apellido = models.CharField(max_length=50,  null=True)
  rut = models.CharField(max_length=50,  null=True)
  email = models.EmailField(max_length=254,  null=True,  unique=True)
  telefono = models.CharField(max_length=15)
  fecha_registro = models.DateTimeField(auto_now=False, auto_now_add=True)
  password = models.CharField(max_length=128, null=True)
  
  def save(self, *args, **kwargs):
    self.username = self.email  # Asignamos el valor del email al username
    super().save(*args, **kwargs)

# Create your models here.



    #OJO Agregar los modelos al admin !!!


