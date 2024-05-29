from django.urls import path 
from .views import (search_book_view, 
                    BookRentalHistoryView,
                    UpdateRentalStatusView) 


app_name  = 'rentals'



urlpatterns = [
    path('', search_book_view, name='main'),
    path('<str:book_id>/', BookRentalHistoryView.as_view(), name='detail'),
    path('<str:book_id>/<pk>/', UpdateRentalStatusView.as_view(), name='update'),

]