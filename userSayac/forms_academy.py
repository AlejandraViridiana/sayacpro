from django import forms
from django.forms import ModelForm 
from .models import Academy,Program,User 

class AcademyModelForm(forms.ModelForm):
    nameAcademy      = forms.CharField(label='Nombre de cuerpo académico:',widget= forms.Textarea(attrs={
        "placeholder": " Cuerpo académico ","class": "academyClass",
        "id": "my-id-nameAcademy","rows": 1,"cols": 22}))
    codeAcademy      = forms.CharField(label='Clave:',required=True,widget= forms.Textarea(attrs={
        "placeholder": " Clave de cuerpo académico",'size': '40',"class": "codeClass",
        "id": "my-id-codeAcademy","rows": 1,"cols": 28}))

    class Meta:
        model = Academy
        fields = ['nameAcademy','codeAcademy']

    def clean(self):
        # data from the form is fetched using super function 
        super(AcademyModelForm, self).clean()        
        # extract the username and text field from the data 
        nameAcademy = self.cleaned_data.get("nameAcademy")
        codeAcademy = self.cleaned_data.get("codeAcademy")
       
        # validations of academy -------------------------------------------------------------------------
        repeatedAcademy = Academy.objects.filter(nameAcademy=nameAcademy).exists()
        if repeatedAcademy:
            self._errors['nameAcademy'] = self.error_class(['El cuerpo académico ya existe'])

        if len(nameAcademy) <10: 
            self._errors['nameAcademy'] = self.error_class(['El cuerpo académico debe contener minimo 10 caracteres'])
        
        # validations of code ------------------------------------------------------------------------------
        if len(codeAcademy) < 5: 
            self._errors['codeAcademy'] = self.error_class(['La clave debe contener mínimo 5 caracteres']) 
        
        if ' ' in codeAcademy or None:
            self._errors['codeAcademy'] = self.error_class(['La clave contiene espacios'])

        repeatedCode = Academy.objects.filter(codeAcademy=codeAcademy).exists()
        if repeatedCode:
            self._errors['codeAcademy'] = self.error_class(['La clave ya existe'])
        # return any errors if found 
        return self.cleaned_data