from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Person
from .forms import Forms
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

class PersonList(ListView):
    model = Person
    template_name = 'home.html'
    context_object_name = 'persons'

class PersonCreate(CreateView):
    model = Person
    template_name = 'create.html'
    form_class = Forms
    success_url = reverse_lazy('home')

class PersonUpdate(UpdateView):
    model = Person
    template_name = 'update.html'
    form_class = Forms
    success_url = reverse_lazy('home')

class PersonDelete(DeleteView):
    model = Person
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class PersonDetail(DetailView):
    model = Person
    template_name = 'detail.html'