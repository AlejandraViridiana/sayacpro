from django.db import models
from django.urls import reverse
from userSayac.models import User 
from projects.models import Project 
from django.core.validators import ValidationError 

class Magazine(models.Model):
    nameMagazine = models.CharField(max_length = 50,verbose_name = "Nombre de revista")  
    editMagazine = models.CharField(max_length = 50,verbose_name = "Editorial")
    countryMagazine = models.CharField(max_length = 50,verbose_name = "País")  
    quartile = (
        ( None, 'Selecciona estado'),
        (' q1 ',' q1 '), 
        (' q2 ',' q2 '), 
        (' q3 ',' q3 '), 
        (' q4 ',' q4 '),  
        )
    quartMagazine = models.CharField(max_length=25,choices=quartile,verbose_name = "Cuartiles")
    referenceMagazine = models.CharField(max_length=100,verbose_name = "Enlace a revista")    
    indMagazine = models.BooleanField(verbose_name = "Indizado")
    indexedMagazine = models.CharField(max_length = 50,verbose_name = "Índice en que se encuentra")   
   
    def __str__(self):
        return self.nameMagazine 


class Article(models.Model): 

    #def validate_file_extension(value):
     #   if not value.name.endswith('.pdf'):
      #      raise ValidationError(u'El archivo ingresado debe ser .pdf')
     
    projectArticle = models.ForeignKey(Project, on_delete=models.PROTECT,verbose_name = "Proyecto")    
    userArticle = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name = "Autor principal")
    otherUserInArticle = models.TextField(max_length=220,verbose_name = "Co-autores") 
    topics = (
        ( None, 'Selecciona estado'),
        (' Medicina ',' Medicina '), 
        (' Inteligencia Artificial','Inteligencia Artificial'),  
        )
    topicArticle = models.CharField(max_length=25,choices=topics,verbose_name = "Tema")
    titleArticle = models.CharField(max_length = 50,verbose_name = "Título de artículo")
    magazineArticle = models.ForeignKey(Magazine, on_delete=models.PROTECT,verbose_name = "Nombre de revista")
    estatus = (
        ( None, 'Selecciona estado'),
        ('En proceso','En proceso'), 
        ('Sometido','Sometido'), 
        ('Liberado','Liberado'), 
        )
    pagesArticle = models.CharField(max_length = 50,verbose_name = "Páginas donde está publicado")
    estatusArticle =models.CharField(max_length=25,choices=estatus,verbose_name = "Estatus")
    volArticle = models.CharField(max_length = 50,verbose_name = "Volumen",default= " N/A ")
    doiArticle = models.CharField(max_length = 50,verbose_name ="DOI",default= " - ")
    archArticle = models.FileField(blank=True, upload_to='archiving/',verbose_name="Archivo (PDF) de articulo")
    createdPubArticle = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titleArticle + ' - ' + self.userArticle.nameUser

    def get_absolute_url(self):
        return reverse("articleSayac:article-detail",kwargs={"id":self.id})