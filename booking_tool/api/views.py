from django.shortcuts import render
from rest_framework import generics, status
from .serializer import TicketSerializer, CreateTickerSerializer
from .models import Ticket
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class TicketView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer



class CreateTickerView (APIView):
    serializer_class = CreateTickerSerializer
    ticket = Ticket

    def post(self, request, format=None):
        # if not self.request.session.exists(self.request.session.session_key):
        #     self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            avs = serializer.data.get('avs')
            booking_from = serializer.data.get('booking_from')
            booking_to = serializer.data.get('booking_to')
            Tec_data = serializer.data.get('Tec_data')
            user = serializer.data.get('user')
            queryset = self.ticket.objects.filter(avs=avs)
            if queryset.exists():
                self.ticket = queryset[0]
                self.ticket.booking_from = booking_from
                self.ticket.booking_to = booking_to
                self.ticket.Tec_data = Tec_data
                self.ticket.user = user
                self.ticket.save(update_fields=['user','booking_from', 'booking_to', 'Tec_data'])
                return Response(TicketSerializer(self.ticket).data, status=status.HTTP_200_OK)
            else:
                self.ticket = self.ticket(avs=avs, user=user, booking_from=booking_from,
                            booking_to=booking_to, Tec_data=Tec_data,
                                )
                self.ticket.save()
            return Response(TicketSerializer(self.ticket).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

