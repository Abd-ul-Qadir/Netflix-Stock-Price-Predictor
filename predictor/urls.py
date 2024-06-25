from.import views 
from django.urls import path 

urlpatterns = [
    path('', views.predict, name='prediction'),
    path('about/', views.about, name='about'),
]