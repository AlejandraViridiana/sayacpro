from django.contrib import admin
from django.urls import include, path
#from articleSayac import views 
from articleSayac.views import ArticleIndexView,ArticleDetailView,ArticleCreateView,ArticleUpdateView,ArticleDeleteView

app_name = 'articleSayac'
urlpatterns = [
   #path('',views.index_view,name='home'),
    path('index',ArticleIndexView.as_view(),name='article-index'),
    path('create',ArticleCreateView.as_view(),name='article-create'), 
    path('<int:id>/',ArticleDetailView.as_view(),name='article-detail'),  
    path('<int:id>/delete',ArticleDeleteView.as_view(),name='article-delete'),
    path('<int:id>/update',ArticleUpdateView.as_view(),name='article-update'), 
]

 
