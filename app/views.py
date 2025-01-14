
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MemorialPage, Memorial

class HomePageView(TemplateView):
  template_name = 'app/home.html'


class AboutPageView(TemplateView):
  template_name = 'app/about.html'


class MemorialListView(ListView):
    model =  Memorial
    template_name = 'app/memorial_list.html'


class MemorialDetailView(DetailView):
  model =  Memorial
  template_name = 'app/memorial_detail.html'


class MemorialCreateView(CreateView):
  model =  Memorial
  fields = ['name', 'description', 'date_of_birth', 'date_of_death', ]
  template_name = 'app/memorial_form.html'


class MemorialUpdateView(UpdateView):
  model =  Memorial
  fields = ['name', 'description', 'date_of_birth', 'date_of_death',]
  template_name = 'app/memorial_form.html'


class MemorialDeleteView(DeleteView):
  model =  Memorial
  template_name = 'app/memorial_confirm_delete.html'
  success_url = '/memorials/'