from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
from books.models import BookTitle


def home_view(request):

    value=Customer.objects.all()
    bt=BookTitle.objects.get(id=1)
    context = {'value': value,
               'bt':bt,
               }
    return render(request, 'main.html', context)