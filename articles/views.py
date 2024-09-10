from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.views.generic.edit import UpdateView , DeleteView , CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
from .models import Articles

class ArticlesListView(LoginRequiredMixin, ListView):
    model = Articles
    template_name = 'articles_list.html'
    login_url = 'login'
    

class ArticlesDetailView(LoginRequiredMixin ,DetailView):
    model = Articles
    template_name = 'article_detail.html'
    login_url = 'login'
    
            
class ArticlesUpdateView(LoginRequiredMixin, UpdateView):
    model = Articles
    fields = ('title','body',)
    template_name='article_edit.html'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
class ArticlesDeleteView(LoginRequiredMixin, DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)
    
class ArticlesCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ('title','body',)
    login_url='login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
