from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import BookTitle
from django.views.generic import ListView, FormView
from .forms import BookTitleForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages

# Create your views here.




class  BookTitleListView(FormView,ListView):
    # model = BookTitle

    template_name = 'books/main.html'
    context_object_name = 'qs'
    form_class = BookTitleForm
    # success_url=reverse_lazy('books:main')
    i_instance = None
    def get_success_url(self):
        return self.request.path
    def get_queryset(self):
        parameter = 's'
        return BookTitle.objects.filter(title__startswith=parameter)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hi'] = 'hello world'
        context['hi2'] = 'hello world2'
         
        return context
    
    def form_valid(self,form):
        self.i_instance  = form.save()
        messages.add_message(self.request, messages.INFO, f"Book title: {self.i_instance.title} has been created  ")
        return super().form_valid(form)
# def book_title_list_view(request):
#     qs = BookTitle.objects.all() 
#     return render(request, 'books/main.html', {'qs':qs})
    def form_invalid(self,form):
            print(form.errors)    
            self.object_list  = self.get_queryset()
            messages.add_message(self.request, messages.ERROR , form.errors)
            return super().form_invalid(form)
    

def book_title_detail_view(request, **kwargs):
    pk= kwargs.get('pk')
    obj = BookTitle.objects.get(pk=pk)
    return  render(request, 'books/detail.html',{'obj':obj})
