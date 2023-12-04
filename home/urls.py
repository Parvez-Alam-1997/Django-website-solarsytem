from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sun', views.sun, name='sun'),
    path('mercury', views.mercury, name='mercury'),
    path('venus', views.venus, name='venus'),
    path('earth', views.earth, name='earth'),
    path('mars', views.mars, name='mars'),
    path('jupiter', views.jupiter, name='jupiter'),
    path('saturn', views.saturn, name='saturn'),
    path('uranus', views.uranus, name='uranus'),
    path('neptune', views.neptune, name='neptune')
]
