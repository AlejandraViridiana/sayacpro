from django import forms
from .models import Article
from projects.models import Project
 
class ArticleModelForm(forms.ModelForm):
    """ 
    projectArticle = forms.ModelChoiceField(label='Proyecto:',queryset=Project.objects.all())
    userArticle        = forms.CharField(label=' Autor principal :', widget= forms.TextInput(
        attrs={"placeholder": " Nombre completo "}))
    otherUserInArticle = forms.CharField( label=' Co-Autores :', required=False,
                                        widget = forms.Textarea(
                                            attrs = {
                                                "placeholder":" Your description",
                                                "class": "new-class-name two",
                                                "id": "my-id-for-textarea",
                                                "rows": 10,
                                                "cols": 110
                                                }
                                            )
                                        )
    topicArticle        = forms.CharField(label='Tema :', widget= forms.TextInput(
        attrs={"placeholder": " - "}))
    titleArticle        = forms.CharField(label='Título de artículo:', widget= forms.TextInput(
        attrs={"placeholder": " - "}))
    magazineArticle        = forms.CharField(label='Revista:', widget= forms.TextInput(
        attrs={"placeholder": " - "}))
    pagesArticle        = forms.CharField(label='Páginas donde está publicado:', widget= forms.TextInput(
        attrs={"placeholder": " - "}))
    estatusArticle        = forms.CharField(label='Estatus:', widget= forms.TextInput(
        attrs={"placeholder": " - "}))
    volArticle        = forms.CharField(label='Volumen:', widget= forms.TextInput(
        attrs={"placeholder": " - "}))
    doiArticle        = forms.CharField(label='DOI:', widget= forms.TextInput(
        attrs={"placeholder": " - "}))
    archArticle        = forms.CharField(label='Archivo (PDF) de articulo:', widget= forms.TextInput(
        attrs={"placeholder": " - "})) 
"""
    class Meta:
        model = Article
        fields = [
            'projectArticle',
            'userArticle',
            'otherUserInArticle', 
            'topicArticle', 
            'titleArticle', 
            'magazineArticle',
            'pagesArticle', 
            'estatusArticle', 
            'volArticle',
            'doiArticle', 
            'archArticle'
        ]           
   
    def clean_archArticle(self,*args,**kwargs):
        archArticle = self.cleaned_data.get("atr")
        if ".pdf" in archArticle:
            return archArticle
        else:
            raise forms.ValidationError("Error en el formulario")













"""
class RawArticleForm(forms.Form):
    userArticle        = forms.CharField(label='un label', widget= forms.TextInput(
        attrs={"placeholder": " Your"}))
    otherUserInArticle = forms.CharField(required=False,
                                        widget = forms.Textarea(
                                            attrs = {
                                                "placeholder":" Your description",
                                                "class": "new-class-name two",
                                                "id": "my-id-for-textarea",
                                                "rows": 20,
                                                "cols": 120
                                                }
                                            )
                                        )
    magazineArticle    = forms.CharField()
    topicArticle       = forms.CharField()
    estatusArticle     = forms.CharField()
    titleArticle       = forms.CharField() 
    """