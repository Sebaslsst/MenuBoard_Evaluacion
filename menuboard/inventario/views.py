from django.shortcuts import render, redirect, get_object_or_404
from .models import Insumo
from django.urls import reverse
from .models import Item

def listar_insumos(request):
    """Vista para listar insumos con filtro opcional."""
    tipo = request.GET.get('tipo', '')  # Obtiene el filtro desde la URL
    if tipo:
        items = Insumo.objects.filter(tipo=tipo)
    else:
        items = Insumo.objects.all()

    return render(request, 'inventario.html', {'items': items})


def guardar_item(request, item_id=None):
    """Vista para agregar o editar un insumo."""
    if request.method == 'POST':
        if item_id:
            item = get_object_or_404(Insumo, id=item_id)
        else:
            item = Insumo()

        item.nombre = request.POST['nombre']
        item.tipo = request.POST['tipo']
        item.cantidad = request.POST['cantidad']
        item.caducidad = request.POST['caducidad']
        item.precio = request.POST['precio']
        item.save()

        return redirect(reverse('listar_insumos'))  # Redirige a la lista después de guardar

    return redirect(reverse('listar_insumos'))
 # Asegúrate de importar tu modelo

def inventario_view(request):
    tipo_filtro = request.GET.get('tipo', '')  # Obtiene el valor del filtro desde la URL
    if tipo_filtro:  # Si el usuario seleccionó un tipo
        items = Item.objects.filter(tipo=tipo_filtro)  # Filtra por el tipo seleccionado
    else:
        items = Item.objects.all()  # Si no hay filtro, muestra todos

    return render(request, 'inventario.html', {'items': items, 'tipo_filtro': tipo_filtro})


def filtrar_item(request):
    tipo = request.GET.get('tipo', '')  # Obtiene el valor del filtro
    if tipo:
        items = Item.objects.filter(tipo=tipo)
    else:
        items = Item.objects.all()

    return render(request, 'inventario.html', {'items': items})