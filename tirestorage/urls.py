from django.http import HttpResponse
from django.urls import path

from . import views as v

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('order/', v.StartOrder.as_view(), name='order'),
]