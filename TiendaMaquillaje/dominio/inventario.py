from TiendaMaquillaje.dominio.especificacionProducto import EspecificacionProducto
from TiendaMaquillaje.dominio.producto import Producto

class Inventario:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if type(producto) == Producto:
            espec = EspecificacionProducto()
            espec.agregar_parametro('id', producto.id)
            if len(list(self.buscar(espec))) == 0:
                self.productos.append(producto)
            else:
                raise Exception('Producto repetido')

    def buscar(self,especificacion):
        for g in self.productos:
            if g.cumple(especificacion):
                yield g