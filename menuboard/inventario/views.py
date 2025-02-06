from django.shortcuts import  render

from inventario.models import Insumo


def filtrar_item(request):
    tipo = request.GET.get('tipo', '')
    if tipo:
        insumos = Insumo.objects.filter(tipo=tipo)  # Filtra por tipo
    else:
        insumos = Insumo.objects.all()  # Muestra todos si no hay filtro

    return render(request, 'inventario.html', {'insumos': insumos})