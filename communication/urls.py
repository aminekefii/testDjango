from django.urls import path
from . import views

urlpatterns = [
    path('msg/<int:id>/', views.afficherMig, name='afficherMig'),
]
