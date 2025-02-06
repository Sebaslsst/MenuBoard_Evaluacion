from django.urls import path

from estadisticas import views
from .views import *

urlpatterns = [
    path('filtrar_item/', filtrar_item, name='filtrar_item'),

]