from django import forms
from django.forms import ModelForm 
from .models import Accounts
  
class AccountsLoginModelForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ['nameAcademy','codeAcademy']

    nameAcademy      = forms.CharField(required=True,
    widget= forms.TextInput(attrs={"type":"text","placeholder":"Correo UABC ","class": "form-control input_user",
        "id": "my-id-emailUser","rows": 1,"cols": 22}))

    codeAcademy      = forms.CharField(required=True,
    widget= forms.TextInput(attrs={"type":"password","placeholder":"Contraseña","class": "form-control input_pass",
        "id": "my-id-passUser","rows": 1,"cols": 22}))

    

    def clean(self):
        # data from the form is fetched using super function   RECURSOS IMPORTANTES ABAJO
        # https://stackoverflow.com/questions/42841431/django-wrap-each-form-element-in-a-div
        # https://stackoverflow.com/questions/15538589/nested-div-inside-django-form
        super(AccountsLoginModelForm, self).clean()        
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