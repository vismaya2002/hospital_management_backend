from django.urls import path
from .views import details,booking,history,checkup


urlpatterns = [
    path('api/<str:pk>',details),
    path('api/booking/<str:pk>',booking),
    path('api/history/<str:pk>/<str:pt>',history),
    path('api/checkup/<str:pk>',checkup),
]