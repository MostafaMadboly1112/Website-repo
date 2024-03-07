from django.shortcuts import render
from rest_framework import generics
from .serializer import TicketSerializer
from .models import Ticket

# Create your views here.
class TicketView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
