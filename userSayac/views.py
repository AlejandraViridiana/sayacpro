from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms_academy import AcademyModelForm
from .forms_programs import ProgramModelForm
from .forms_user import UserModelForm
from .models import Academy,Program,User
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)


class AcademyIndexView(ListView): 
    template_name = 'academy/academy_index.html'
    queryset = Academy.objects.all()
################################################ 
class AcademyCreateView(CreateView): 
    template_name = 'academy/academy_create.html'
    form_class = AcademyModelForm
    queryset = Academy.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)
############################################################
class AcademyDetailView(DetailView): 
    template_name = 'academy/academy_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Academy, id=id_)
############################################################
class AcademyUpdateView(UpdateView): 
    template_name = 'academy/academy_update.html'
    form_class = AcademyModelForm
    queryset = Academy.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Academy, id=id_)
############################################################
class AcademyDeleteView(DeleteView): 
    template_name = 'academy/academy_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Academy, id=id_)

    def get_success_url(self): 
        return reverse('userSayac:academy-index')


class ProgramIndexView(ListView): 
    template_name = 'program/program_index.html'
    queryset = Program.objects.all()
############################################################
class ProgramCreateView(CreateView): 
    template_name = 'program/program_create.html'
    form_class = ProgramModelForm #falta validar el registro de los datos
    queryset = Program.objects.all() 

    def form_valid(self, form):
        return super().form_valid(form)   
############################################################
class ProgramDetailView(DetailView): 
    template_name = 'program/program_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Program, id=id_)
############################################################
class ProgramUpdateView(UpdateView): 
    template_name = 'program/program_update.html'
    form_class = ProgramModelForm
    queryset = Program.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Program, id=id_)
############################################################
class ProgramDeleteView(DeleteView):  
    template_name = 'program/program_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Program, id=id_)

    def get_success_url(self): 
        return reverse('userSayac:program-index')


class UserIndexView(ListView): 
    template_name = 'user/user_index.html'
    queryset = User.objects.all()
############################################################
class UserCreateView(CreateView): 
    template_name = 'user/user_create.html'
    form_class = UserModelForm
    queryset = User.objects.all() 

    def form_valid(self, form):
        return super().form_valid(form)   
############################################################
class UserDetailView(DetailView): 
    template_name = 'user/user_detail.html' 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)
############################################################
class UserUpdateView(UpdateView): 
    template_name = 'user/user_update.html'
    form_class = UserModelForm
    queryset = User.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)    

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)
############################################################
class UserDeleteView(DeleteView):
    template_name = 'user/user_delete.html'  

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(User, id=id_)

    def get_success_url(self): 
        return reverse('User:user-index')




"""
def detailAcademy(request, indexId): 
    obj = get_object_or_404(Academy,id=indexId) 
    context = { 
        'obj':obj
    }
    return render(request, "academys/detailAcademy.html", context)

def deleteAcademy(request, indexId): 
    obj = get_object_or_404(Academy,id=indexId) 
    if request.method == "POST":
      obj.delete()

    context = { 
        'obj':obj
    }
    return render(request, "academys/deleteAcademy.html", context)

def indexAcademy(request):
   #obj = Academy.objects.get(id=1)   
    obj = Academy.objects.all() 
    context = { 
        'obj':obj,  
    }
    return render(request, "academys/indexAcademy.html", context)

def createAcademy(request,*args,**kwargs):
    form = academyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = academyForm() 
    context = { 
        'form':form
    } 
    return render(request, "academys/createAcademy.html", context)


def render_inicial_data(request):
    #establecer valores de defecto en forma
    initial_data = {
      'attr de BD' = "valor por defecto para el form"
    }
    obj=tabla.objects.get(id=1)
    form = academyForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = academyForm() 
    context = { 
    #'Autor':obj.userArticle.nameUser
        'form':form
    } 
    return render(request, "model/createMODELO.html", context)
"""