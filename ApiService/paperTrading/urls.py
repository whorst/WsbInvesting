from django.urls import path
from ApiService.paperTrading.views.valid_position_views import ValidPosition
from ApiService.paperTrading.views.valid_position_views import Calls
from ApiService.paperTrading.views.valid_position_views import Puts
from ApiService.paperTrading.views.account_views import Account
urlpatterns = [
    path(r'position/<ticker>/', ValidPosition.as_view()),
    path(r'calls/', Calls.as_view()),
    path(r'puts/', Puts.as_view()),
    path(r'account/hello/', Account.as_view())
]

