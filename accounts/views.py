from django.shortcuts import render

from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Accounts
from .forms_Login import AccountsLoginModelForm
from .forms_Register import AccountsRegisterModelForm 
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)

class AccountsCreateView(CreateView): 
    template_name = 'register.html'
    form_class = AccountsRegisterModelForm
    queryset = Accounts.objects.all() 

    def form_valid(self, form):
        return super().form_valid(form)



class AccountsLoginView(CreateView): 
    template_name = 'login.html' 
    form_class = AccountsLoginModelForm
    queryset = Accounts.objects.all() 

    def form_valid(self, form):
        return super().form_valid(form)