from django import forms
from django.forms import ModelForm 
from .models import Academy,Program,User 

class UserModelForm(forms.ModelForm):
    numberUser      = forms.CharField(label='Matrícula:',required=True,
    widget= forms.Textarea(attrs={"placeholder": " -  ","class": "xClass",
    "id": "my-id-nameAcademy","rows": 1,"cols": 22}))
    nameUser      = forms.CharField(label='Nombre completo:',required=True,
    widget= forms.Textarea(attrs={"placeholder": "  -  ",'size': '40',"class": "xClass",
    "id": "my-id-nameUser   ","rows": 1,"cols": 28}))
    programUser  = forms.CharField(label='Nombre del programa educativo:',required=True,
    widget= forms.Textarea(attrs={"placeholder": "  -  ",'size': '40',"class": "xClass",
    "id": "my-id-programUser   ","rows": 1,"cols": 28}))
    academyUser  = forms.CharField(label='Nombre de cuerpo académico:',required=True,
    widget= forms.Textarea(attrs={"placeholder": "  -  ",'size': '40',"class": "xClass",
    "id": "my-id-academyUser   ","rows": 1,"cols": 28}))
    estatusUser  = forms.CharField(label='Clave:',required=True,
    widget= forms.Textarea(attrs={"placeholder": "  -  ",'size': '40',"class": "xClass",
    "id": "my-id-estatusUser","rows": 1,"cols": 28}))
    emailUser    = forms.CharField(label='Correo UABC:',required=True,
    widget= forms.Textarea(attrs={"placeholder": "  -  ",'size': '40',"class": "xClass",
    "id": "my-id-emailUser","rows": 1,"cols": 28}))
    rolUser      = forms.CharField(label='Rol de usuario:',required=True,
    widget= forms.Textarea(attrs={"placeholder": "  -  ",'size': '40',"class": "xClass",
    "id": "my-id-rolUser   ","rows": 1,"cols": 28}))

    class Meta:
        model = User
        fields = ['numberUser','nameUser','programUser','academyUser','estatusUser','emailUser','rolUser']

    def clean(self):
        # data from the form is fetched using super function 
        super(UserModelForm, self).clean()        
        # extract the username and text field from the data 
        numberUser = self.cleaned_data.get("numberUser")
        nameUser = self.cleaned_data.get("nameUser")
        programUser = self.cleaned_data.get("programUser")
        academyUser = self.cleaned_data.get("academyUser")
        estatusUser = self.cleaned_data.get("estatusUser")
        emailUser = self.cleaned_data.get("emailUser")
        rolUser = self.cleaned_data.get("rolUser")