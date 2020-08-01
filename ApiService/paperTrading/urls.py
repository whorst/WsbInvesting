from django.urls import path, include
from .views import ValidPosition

urlpatterns = [
    path(r'getByTicker/<ticker>/', ValidPosition.as_view()),
    path(r'getByIsCall/<callsOrPuts>/', ValidPosition.as_view())
]
