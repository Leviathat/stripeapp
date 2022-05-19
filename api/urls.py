from django.urls import path
from api.views import *

urlpatterns = [
    path('item/<int:pk>/', article),
    path('buy/<int:pk>/', buy),
]
