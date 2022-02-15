from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path("guide",views.guides,name='guides'),
    path('destinations',views.destinations,name='destinations'),
    path('booking',views.booking,name="booking"),
    path('booked',views.booked,name="booked"),
    path('search',views.search,name='search'),
    path('index',views.index,name='index'),
]