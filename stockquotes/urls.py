from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about.html', views.about,name="about"),
    path('add_quote.html', views.add_quote,name="add_quote"),
    path('delete/<quote_id>', views.delete,name="delete"),
    path('delete_stock.html', views.delete_stock,name="delete_stock"),


]