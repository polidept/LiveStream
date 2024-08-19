from django.urls import path
from . views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('browse/', BrowseView.as_view(), name='browse'),

]