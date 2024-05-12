from django.urls import path 
from .views import  BookTitleDetailView,BookTitleListView



app_name ='books'

urlpatterns = [
    path('',BookTitleListView.as_view(),{'letter':None}, name='main'),
    path('<str:letter>/',BookTitleListView.as_view(), name='main'),
    path('<str:letter>/<slug>/', BookTitleDetailView.as_view(), name="detail")

]