from django.http import HttpResponseRedirect
from django.shortcuts import render
from customers.models import Customer
from books.models import BookTitle
from django.http import JsonResponse

from django.views.generic import TemplateView


def change_theme(request):

    print(request.session['is_dark_mode'])
    print(type (request.session))
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = False
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

"""
create dashboard view - template view
create seperate data view with JsonResponse
create js file -> attach it to the template -> load the data to js
use the data to draw charts

charts:
1) book titles vs books (bar)
2) book title count by publisher (pie)
3) books by status (pie)
4) publishers vs customers (bar)

"""

class DashboardView(TemplateView):
    template_name  = 'dashboard.html'

def chart_data(request):
    return JsonResponse({'msg':'hello world chart data view'})












# def home_view(request):

#     value=Customer.objects.all()
#     bt=BookTitle.objects.get(id=1)
#     context = {'value': value,
#                'bt':bt,
#                }
#     return render(request, 'main.html', context)