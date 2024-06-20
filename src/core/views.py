from django.http import HttpResponseRedirect
from django.shortcuts import render
from customers.models import Customer
from books.models import Book,BookTitle
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.db.models import Count, Sum
from rentals.models import Rental
from publishers.models import Publisher
from rentals.rental_choices import STATUS_CHOICES
from .forms import LoginForm, OTPForm
from django.contrib.auth import login, authenticate, logout
from  django.contrib import messages
from .utils import send_otp


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            username  =form.cleaned_data.get('username')
            password  =form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                send_otp(request)
                print('ok, sending otp')
            else:
                messages.add_message(request,messages.ERROR, 'Invalid username or password')
    context = {
        'form': form,
    }
    return render(request,'login.html', context )




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
    data=[]
    # 1) book titles vs books (bar)
    all_books = len(Book.objects.all())
    all_book_titles = len(BookTitle.objects.all())
    data.append({
        'labels':['books','book titles'],
        'data':[all_books, all_book_titles],
        'description':'unique book titles vs books',
        'type':'bar',
    })

    # 2) book title count by publisher (pie)
    titles_by_publisher = BookTitle.objects.values('publisher__name').annotate(Count('publisher__name'))
    publisher_names  = [x['publisher__name'] for x in titles_by_publisher]
    publisher_name_count = [x['publisher__name__count'] for x in titles_by_publisher ]
    data.append({
        'labels':publisher_names,
        'data':publisher_name_count,
        'description':'book title count by publisher',
        'type':'pie',
    })
    # 3) books by status (pie)
    book_by_status = Rental.objects.values('status').annotate(Count('book__title'))
    book_title_count = [x['book__title__count'] for x in book_by_status]
    status_keys = [x['status'] for x in book_by_status]
    status  =  [dict(STATUS_CHOICES)[key] for key in status_keys]
    data.append({
        'labels':status,
        'data':book_title_count,
        'description':'book by status',
        'type':'pie',
    })
    # 4) publishers vs customers (bar)
    customers = len(Customer.objects.all())
    publishers = len(Publisher.objects.all())
    data.append(
        {
        'labels':['customers','publishers'],
        'data':[customers, publishers],
        'description':'customers vs publishers',
        'type':'bar',
        }
    )
    print(data)
    return JsonResponse({'data':data})












# def home_view(request):

#     value=Customer.objects.all()
#     bt=BookTitle.objects.get(id=1)
#     context = {'value': value,
#                'bt':bt,
#                }
#     return render(request, 'main.html', context)