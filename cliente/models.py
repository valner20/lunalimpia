from django.db import models
from django.contrib.auth.models import AbstractUser
    
class Profesional(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[]
    )
    cedula = models.CharField(max_length=100, unique=True)
    USERNAME_FIELD = 'cedula'        
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, null=True)
    cedula = models.CharField(max_length=100, null=True)
    correo = models.CharField(max_length=100, null=True)
    video = models.TextField(null=True)
    ##cedula y correo
    def __str__(self):
        return self.nombre

class Turno(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='citas')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='citas')
    fecha = models.DateField()
    hora = models.CharField(max_length=100)
    valor= models.IntegerField(null=True)

    class Meta:
        unique_together = ('profesional', 'fecha', 'hora') 

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.cliente} con {self.profesional}"
