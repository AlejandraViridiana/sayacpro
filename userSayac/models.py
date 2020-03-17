from django.db import models 
from django.urls import reverse
from accounts.models import Accounts

class Academy(models.Model):
    nameAcademy = models.CharField(max_length=100,verbose_name = "Cuerpo académico")  
    codeAcademy = models.CharField(blank=False,max_length=100,verbose_name = "Clave")  
    createdPubAcademy = models.DateTimeField(auto_now_add=True,verbose_name="Fecha")
    
    def __str__(self):
        return self.nameAcademy + " - " + self.codeAcademy

  #  def get_absolute_url(self):
   #     return reverse("detailAcademy",kwargs={"id":self.id}) 
    
    def get_absolute_url(self):
        return reverse("userSayac:academy-detail",kwargs={"id":self.id})
 


class Program(models.Model):
    nameProgram = models.CharField(max_length=100,verbose_name = "Nombre de programa") 
    numberProgram = models.CharField(max_length=100,verbose_name = "Código de programa") 
    respProgram = models.PositiveIntegerField(verbose_name = "Responsable en proyectos")
    partProgram = models.PositiveIntegerField(verbose_name = "Participación en proyectos")
    createdPubProgram = models.DateTimeField(auto_now_add=True,verbose_name="Fecha")

    def __str__(self):
        return self.nameProgram

    def get_absolute_url(self):
        return reverse("userSayac:program-detail",kwargs={"id":self.id})


class User(models.Model):
    numberUser = models.CharField(max_length = 20,verbose_name = "Código de empleado",blank=True, null=True) 
    accountUser = models.ForeignKey(Accounts, on_delete=models.PROTECT,verbose_name = "Cuenta")
    programUser = models.ForeignKey(Program, on_delete=models.PROTECT,verbose_name = "Programa educativo")
    academyUser =  models.ForeignKey(Academy, on_delete=models.PROTECT,verbose_name = "Cuerpo académico") 
    estatuSelect = (
        ( None, 'Selecciona estado'),
        ('Activo','Activo'), 
        ('Inactivo','Inactivo'), 
        )
    estatusUser = models.CharField(max_length=25,choices=estatuSelect,verbose_name = "Estatus") 
    rolSelect = (
        ( None, 'Selecciona estado'),
        ('Profesor/Investigador','Profesor/Investigador'), 
        ('Técnico académico','Técnico académico'),  
        ('Estudiante licenciatura','Estudiante licenciatura'),  
        ('Estudiante postgrado','Estudiante postgrado'), 
        )
    rolUser = models.CharField(max_length=25,choices=rolSelect,verbose_name = "Rol en UABC",blank=True, null=True) 
    createdPubUser = models.DateTimeField(auto_now_add=True,verbose_name="Fecha") 
     
    def __str__(self):
        return self.accountUser.firstName +" - "+ self.accountUser.lastName 

    def get_absolute_url(self):
        return reverse("userSayac:user-detail",kwargs={"id":self.id})


