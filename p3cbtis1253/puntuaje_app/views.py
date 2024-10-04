from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def contactos(request):
    return render(request,"contactos.html")

def empleado(request):
    return render(request,"empleado.html")

# Tablas

def sucursal(request):
    return render(request,"sucursal.html")

def provedor(request):
    return render(request,"provedor.html")

def producto(request):
    return render(request,"producto.html")

def venta(request):
    return render(request,"venta.html")





