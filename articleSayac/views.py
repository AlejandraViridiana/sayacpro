from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Article
from .forms import ArticleModelForm 
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)

############################################################
class ArticleIndexView(ListView): 
    template_name = 'article/article_index.html'
    queryset = Article.objects.all()
############################################################
class ArticleCreateView(CreateView): 
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() 

    def form_valid(self, form):
        return super().form_valid(form)   
############################################################
class ArticleDetailView(DetailView): 
    template_name = 'article/article_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
############################################################
class ArticleUpdateView(UpdateView): 
    template_name = 'article/article_update.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
############################################################
class ArticleDeleteView(DeleteView): 
    template_name = 'article/article_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self): 
        return reverse('articleSayac:article-index')


"""
def indexPageView(request,*args,**kwargs):
    return render(request,"index.html",{})
 
def indexArticle(request,*args,**kwargs):
    obj = Article.objects.get(id=1)
    context = {
      #'Autor':obj.userArticle.nameUser
        'obj':obj
    }
    return render(request, "indexArticles.html", context)


def createArticle(request,*args,**kwargs):
    my_form = RawArticleForm()
    if request.method == "POST":
        my_form = RawArticleForm(request.POST)
        if my_form.is_valid():
            Article.objects.create(**my_form.cleaned_data)
    context = {
    }
    return render(request, "createArticles.html", context)
"""