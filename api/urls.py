from django.contrib import admin
from django.urls import path

from .views import SticticCreateView, SticticShowView, reset


urlpatterns = [
    path('statistic/create/', SticticCreateView.as_view()),
    path('statistic/get/', SticticShowView.as_view()),
    path('statistic/delete/', reset),
]
