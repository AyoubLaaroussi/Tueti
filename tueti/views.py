from django.shortcuts import render
from tueti.models import Tuet
from tueti.serializers import TuetSerializer

from rest_framework import generics

from django.views.generic import ListView


# Create your views here.
class TuetList(ListView):

    context_object_name = 'tuets'

    def get_queryset(self):
        queryset =  Tuet.objects.all()
        return queryset
    

