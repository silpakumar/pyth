from django.urls import path
from.import views
urlpatterns=[
    path('home1/',views.index),
    path('home/',views.index1)
]