import os
import random
from FabricaPanaderia.dominio.inventario import Inventario
from FabricaPanaderia.dominio.producto import Producto
from FabricaPanaderia.infraestructura.persistenciaProducto import PersistenciaProducto

inventario = Inventario()

if __name__ == '__main__':
    nombres = ['pan', 'almojabana', 'roscon', 'chicharon', 'reina', 'tostada']
    formas = {
        'pan': ['pequeño', 'mediano', 'grande', 'suave'],
        'almojabana': ['pequeño', 'mediano', 'suave'],
        'roscon': ['pequeño', 'mediano', 'grande', 'suave'],
        'chicharon': ['mediano', 'medio duro', 'duro'],
        'reina': ['pequeño', 'mediano', 'grande', 'suave'],
        'tostada': ['mediano', 'dura'],
    }
    precios = [1000, 2000, 500, 800, 1500, 4000]
    cantidad_productos = random.randint(100, 1000)
    nombre = random.choice(nombres)
    forma = random.choice(formas[nombre])
    precio = random.choice(precios)
    g = Producto(nombre, forma, precio)
    PersistenciaProducto.save(g)
    PersistenciaProducto.save_json(g)
    inventario = Inventario()
    inventario_json = Inventario()
    for file in os.listdir("./files"):
        if '.gui' in file:
            inventario.agregar_producto(PersistenciaProducto.load(file))
        if '.json' in file:
            inventario_json.agregar_producto(PersistenciaProducto.load_json(file))
    for g in inventario.productos:
        PersistenciaProducto.save(g)
        PersistenciaProducto.save_json(g)