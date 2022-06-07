from django.urls import path
from . import views

urlpatterns = [
    path('callback/', views.callback, name='callback'), # add this line
    path('liftpage/', views.liftpage, name='liftpage'), # add this line
   
]


