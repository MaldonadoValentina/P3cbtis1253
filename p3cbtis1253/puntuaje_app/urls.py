from django.urls import path
from . import views
urlpatterns = [
    path("",views.index, name= "index"),
    path("contactos/",views.contactos, name= "contactos"),
    path("empleado/",views.empleado, name= "empleado"),
    # Tablas
    path("sucursal/",views.sucursal, name= "sucursal"),
    path("provedor/",views.provedor, name= "provedor"),
    path("producto/",views.producto, name= "producto"),
    path("venta/",views.venta, name= "venta"),

]
