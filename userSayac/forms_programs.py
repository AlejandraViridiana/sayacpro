from django import forms
from django.forms import ModelForm 
from .models import Academy,Program,User 

class ProgramModelForm(forms.ModelForm):
    nameProgram      = forms.CharField(label='Nombre del programa educativo:',widget= forms.Textarea(attrs={
        "placeholder": " Programa educativo ","class": "programClass",
        "id": "my-id-nameAcademy","rows": 2,"cols": 32}))
    numberProgram      = forms.CharField(label='Clave de programa educativo:',required=True,widget= forms.Textarea(attrs={
        "placeholder": " Clave de Programa educativo",'size': '40',"class": "numberClass",
        "id": "my-id-codeAcademy","rows": 1,"cols": 28}))
    respProgram      = forms.CharField(label='Total de proyectos liderados:',required=True,widget= forms.Textarea(attrs={
        "placeholder": " - ",'size': '40',"class": "respClass",
        "id": "my-id-respProgram","rows": 1,"cols": 28}))
        #la variable de arriba incrementa cada que se registra una persona como responsable en un proyecto
        #debe haber un query que incremente la cantidad total.
    partProgram      = forms.CharField(label='Total de proyectos participados:',required=True,widget= forms.Textarea(attrs={
        "placeholder": " - ",'size': '40',"class": "partClass",
        "id": "my-id-partProgram","rows": 1,"cols": 28}))  
#más adelante en un detail de este módulo, poner por semestres de forma ejecutiva gráficas, para la cantidad de
#proyectos participados y liderados.
    class Meta:
        model = Program
        fields = ['nameProgram','numberProgram','respProgram','partProgram']

    def clean(self):
        # data from the form is fetched using super function 
        super(ProgramModelForm, self).clean()        
        # extract the username and text field from the data 
        nameProgram = self.cleaned_data.get("nameProgram")
        numberProgram = self.cleaned_data.get("numberProgram")
        respProgram = self.cleaned_data.get("respProgram")
        partProgram = self.cleaned_data.get("partProgram")
       
    