from django.shortcuts import redirect, render
from inventario.models import Inventario



def home(request):
    return render(request, "home.html")

def login(request):
    return render(request,'login.html')


def inventario(request):
    return render(request,'inventario.html')


def registrate(request):
    return render(request,'registrate.html')


def inicio(request):
    return render(request,'inicio.html')


def guardar_item(request, id=None):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        caducidad = request.POST.get('caducidad')
        precio = request.POST.get('precio')

        if id:
            item = Inventario.objects.get(id=id)
        else:
            item = Inventario()

        item.nombre = nombre
        item.cantidad = cantidad
        item.caducidad = caducidad
        item.precio = precio
        item.save()

        return redirect('inventario')  # O la vista correspondiente
    return render(request, 'inventario.html')


def menu(request):
    return render(request, 'menu.html')


def reservacion(request):
    return render(request, 'reservacion.html')


def compra(request):
    return render(request, 'compra.html')


def comienzo(request):
    return render(request, 'project_content/comienzo.html')


def pedido(request):
    return render(request,'pedido.html')