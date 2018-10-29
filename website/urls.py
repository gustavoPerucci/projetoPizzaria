from django.conf.urls import url, include
from django.urls import path
from .views import (
    home,
)

urlpatterns = [
    path('', home, name='website_home'),    
]