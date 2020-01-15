from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

class Project(models.Model):
    selectProject = (
        ( None, 'Selecciona estado'),
        ('Interno','Interno'), 
        ('Externo','Externo'), 
        ('Convenio','Convenio'),  
        ('UABC','UABC'),    
        )
    typeProject = models.CharField(blank=True,max_length=25,choices=selectProject,verbose_name = " Tipo de proyecto")
    
    #El tipo lo haré que se automatice con el tiempo, para que desde la página decida el tipo de proyecto
    # y le aparezca un formulario que corresponda, de momento será genérico para que sea un mismo formulario
    # independientemente del tipo de proyecto
    titleProject = models.CharField(blank=True,null=True,max_length = 50,verbose_name = "Título de proyecto", default='Proyecto')
    announcementProject = models.CharField(blank=True,max_length=100,verbose_name = " Convocatoria (Si aplica)")
    amountProject = models.CharField(blank=True,max_length = 50,verbose_name = "Monto")
    responsableProject = models.CharField(blank=True,max_length = 50,verbose_name = "Responsable técnico") 
    partProject = models.TextField(blank=True,max_length=220,verbose_name = "Participantes") 
    #participantes.. aquí adebe hacer una búsqueda por ID y añadirlos a los que necesite.
    
    codeProject = models.CharField(verbose_name = "Clave",blank=True,max_length=100)
    vigenciaProject = models.DateField(verbose_name = "Vigencia hasta")
    state = (
        ( None, 'Selecciona estado'),
        ('Vigente','Vigente'), 
        ('No vigente','No vigente'), 
        ('Concluido','No Concluido'),  
        )
    stateProject = models.CharField(blank=True,max_length=25,choices=state,verbose_name = "Estado del proyecto")

    def __str__(self):
        return self.titleProject + " - Clave: - " + self.codeProject

