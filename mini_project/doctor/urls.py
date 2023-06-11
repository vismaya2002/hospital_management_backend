from django.urls import path
from .views import details,booking,history,checkup,ptdetails,docinout


urlpatterns = [
    path('api/<str:pk>',details),
    path('api/patient/<str:pk>',ptdetails),
    path('api/booking/<str:pk>',booking),
    path('api/history/<str:pk>/<str:pt>',history),
    path('api/checkup/<str:pk>',checkup),
    path('api/doctor/<str:pk>/<str:pt>',docinout),
]