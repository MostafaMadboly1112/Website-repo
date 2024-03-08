from django.db import models



# Create your models here.
class Ticket(models.Model):
    avs = models.CharField(max_length=16, default="", unique=True)
    user = models.CharField(max_length=30)
    booking_from = models.DateTimeField()
    booking_to = models.DateTimeField()
    Tec_data = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

