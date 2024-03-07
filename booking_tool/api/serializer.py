from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'avs', 'user', 'booking_from', 
                  'booking_to','Tec_data', 'created_at')