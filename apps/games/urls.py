from django.urls import path
from .views import *

urlpatterns = [
    path('game_list/', GameListView.as_view(), name='game_list'),
    path('game_detail/', GamesDetail.as_view(), name='game_detail'),
]