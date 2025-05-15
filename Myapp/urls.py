from django.urls import path
from . import views #call index

urlpatterns = [
   path('home/',views.indexview, name='home'),
]