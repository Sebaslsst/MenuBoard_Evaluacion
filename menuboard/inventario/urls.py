from django.urls import path
from .views import (listar_insumos, guardar_item,
                    filtrar_item, inventario_view)
urlpatterns = [
    path('listar/', listar_insumos, name='listar_insumos'),
    path('inventario/guardar/', guardar_item, name='guardar_item'),
    path('inventario/guardar/<int:item_id>/', guardar_item, name='guardar_item'),
    path('inventario/', inventario_view, name='inventario'),
    path('filtrar/', filtrar_item, name='filtrar_item'),

]