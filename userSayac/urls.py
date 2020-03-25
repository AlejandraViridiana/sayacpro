from django.urls import path
from userSayac.views import AcademyIndexView,AcademyCreateView,AcademyDetailView,AcademyUpdateView,AcademyDeleteView
from userSayac.views import ProgramIndexView,ProgramCreateView,ProgramDetailView,ProgramUpdateView,ProgramDeleteView
from userSayac.views import UserIndexView,UserCreateView,UserDetailView,UserUpdateView,UserDeleteView

app_name = 'userSayac'
urlpatterns = [ 
    #---------------- Path para academia
    path('academy/index',AcademyIndexView.as_view(),name='academy-index'),
    path('academy/create',AcademyCreateView.as_view(),name='academy-create'), 
    path('academy/<int:id>/',AcademyDetailView.as_view(),name='academy-detail'),  
    path('academy/<int:id>/delete',AcademyDeleteView.as_view(),name='academy-delete'),
    path('academy/<int:id>/update',AcademyUpdateView.as_view(),name='academy-update'), 

    #---------------- Path para Programas
    path('program/index',ProgramIndexView.as_view(),name='program-index'),
    path('program/create',ProgramCreateView.as_view(),name='program-create'), 
    path('program/<int:id>/',ProgramDetailView.as_view(),name='program-detail'),  
    path('program/<int:id>/delete',ProgramDeleteView.as_view(),name='program-delete'),
    path('program/<int:id>/update',ProgramUpdateView.as_view(),name='program-update'), 

    #---------------- Path para usuario
    path('user/index',UserIndexView.as_view(),name='user-index'),
    path('user/create',UserCreateView.as_view(),name='user-create'), 
    path('user/<int:id>/',UserDetailView.as_view(),name='user-detail'),  
    path('user/<int:id>/delete',UserDeleteView.as_view(),name='user-delete'),
    path('user/<int:id>/update',UserUpdateView.as_view(),name='user-update'), 

]