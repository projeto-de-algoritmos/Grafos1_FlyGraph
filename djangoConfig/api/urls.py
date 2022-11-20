from django.urls import path
from . import views

urlpatterns = [
    path('get-data/', views.getData),
    path('airports/', views.getAirports),
    path('check-graph/', views.checkGraph),


]
