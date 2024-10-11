from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('index.html', views.main, name='home'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('contact.html', views.contact, name='contact'),
]