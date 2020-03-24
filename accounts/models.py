from django.db import models
from django.urls import reverse  

class Accounts(models.Model):
    firstName = models.CharField(max_length = 50,verbose_name = "Nombre(s)")  
    lastName = models.CharField(max_length = 50,verbose_name = "Apellido(s)")
    emailAccount = models.EmailField(max_length=100,verbose_name = "Correo UABC",blank=True, null=True) 
    passwordAccount = models.CharField(max_length = 50,verbose_name = "Contraseña")   
    confirmPasswordAccount = models.CharField(max_length = 50,verbose_name = "Confirmar Contraseña")   
   
    def __str__(self):
        return self.emailAccount