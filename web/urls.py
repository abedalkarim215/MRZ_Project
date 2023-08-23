from django.urls import path
from .views import (
    Landing,
    MRZ_Extractor,
    Ticket,
)
urlpatterns = [
    path('',Landing.as_view(),name='landing'),
    path('mrz/',MRZ_Extractor.as_view(),name='MRZ_extractor'),
    path('ticket/',Ticket.as_view(),name='ticket'),
]