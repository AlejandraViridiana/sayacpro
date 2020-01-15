from django.db import models

class Magazine(models.Model):

# existe algo que proteger.. si o no... si es si para los que si tienen algo que proteger entonces ya se autoriza
# No cumple... y que lo vea el autor.. 
# Se autoriza la publicación... 
# Medida preventiva tener eso en mente... puede que le diga que no se publique y no tenga que cambiar.. 
# Coordinador y si da respuesta.. responsable de propiedad intelectual de la facultad..

    nameMagazine = models.CharField(max_length = 50,verbose_name = "Nombre de revista")
    referenceMagazine = models.CharField(max_length=100,verbose_name = "Enlace a revista")

    def __str__(self):
        return self.nameMagazine 
