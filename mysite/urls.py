from django.urls import path

from mysite import views

urlpatterns = [
    path('', views.index),
    path('Needs', views.Needs),
    path('status', views.status),
    path('Geography', views.Geography),
    path('Skills', views.Skills),
    path('LastVac', views.LastVac),
]
