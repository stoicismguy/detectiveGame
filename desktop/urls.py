from django.urls import path
from .views import *

urlpatterns = [
    path('', desktop_view, name='desktop')
]
