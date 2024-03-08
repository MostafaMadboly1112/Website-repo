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


#'avs','booking_from','booking_to','Tec_data')

class CreateTickerView (APIView):
    serializer_class = CreateTickerSerializer
    

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
            queryset = Ticket.objects.filter(avs=avs)
            if queryset.exists():
                Ticket = queryset[0]
                Ticket.booking_from = booking_from
                Ticket.booking_to = booking_to
                Ticket.Tec_data = Tec_data
                Ticket.user = user
                Ticket.save(update_fields=['user','booking_from', 'booking_to', 'Tec_data'])
                return Response(TicketSerializer(Ticket).data, status=status.HTTP_200_OK)
            else:
                Ticket = Ticket(avs=avs, user=user, booking_from=booking_from,
                            booking_to=booking_to, Tec_data=Tec_data,
                                )
                Ticket.save()
            return Response(TicketSerializer(Ticket).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

