from django.shortcuts import render
from rest_framework import viewsets
from .serializers import foodstuffSerializer
from .models import foodstuff

# Create your views here.

class foodstuffviewset(viewsets.ModelViewSet):
    queryset = foodstuff.objects.all().order_by('Name')
    serializer_class = foodstuffSerializer