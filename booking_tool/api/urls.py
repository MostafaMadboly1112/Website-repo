from django.urls import path
from .views import TicketView,CreateTickerView

urlpatterns = [
    path('', TicketView.as_view() ),
    path('create-ticket', CreateTickerView.as_view())
]
