from django.urls import path
from .views import vodhome


urlpatterns = [
    path('', vodhome, name='vodhome-list'),
]
