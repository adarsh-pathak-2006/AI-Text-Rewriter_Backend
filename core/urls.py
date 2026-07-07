from django.urls import path
from core.views import *

urlpatterns = [
    path('all/', TotalEntriesAPI.as_view(), name='total'),
    path('output/<int:pk>/', FinalOutputAPI.as_view(), name='output'),
]
