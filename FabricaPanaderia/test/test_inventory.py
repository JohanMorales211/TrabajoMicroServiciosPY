import random
from FabricaPanaderia.dominio.producto import Producto
from FabricaPanaderia.dominio.inventario import Inventario
from FabricaPanaderia.dominio.especificacionProducto import EspecificacionProducto

def test_buscar():
    nombres = ['pan', 'almojabana', 'roscon', 'chicharon','reina','tostada']
    formas = {
        'pan': ['pequeño', 'mediano', 'grande', 'suave'],
        'almojabana': ['pequeño', 'mediano', 'suave'],
        'roscon': ['pequeño', 'mediano', 'grande', 'suave'],
        'chicharon': ['mediano', 'medio duro','duro'],
        'reina': ['pequeño', 'mediano', 'grande', 'suave'],
        'tostada': ['mediano', 'dura'],
    }
    inv = Inventario()
    for nombre in nombres:
        for forma in formas[nombre]:
            inv.agregar_producto(Producto("almojabana", forma, 2000))
        especificacion = EspecificacionProducto()
        especificacion.agregar_parametro('nombre', nombre)
        for producto in inv.buscar(especificacion):
            assert producto is not None
        assert len(list(inv.buscar(especificacion))) >= 0

def test_fuzzing_buscar():
    nombres = ['pan', 'almojabana', 'roscon', 'chicharon', 'reina', 'tostada']
    formas = {
        'pan': ['pequeño', 'mediano', 'grande', 'suave'],
        'almojabana': ['pequeño', 'mediano', 'suave'],
        'roscon': ['pequenio', 'mediano', 'grande', 'suave'],
        'chicharon': ['mediano', 'medio duro', 'duro'],
        'reina': ['pequeño', 'mediano', 'grande', 'suave'],
        'tostada': ['mediano', 'dura'],
    }
    precios = [1000, 2000, 500, 800, 1500, 4000]
    cantidad_productos = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_productos):
        nombre = random.choice(nombres)
        forma = random.choice(formas[nombre])
        precio = random.choice(precios)
        if i % 10 == 0:
            especificacion = EspecificacionProducto()
            especificacion.agregar_parametro('nombre', nombres)
            especificacion.agregar_parametro('forma', formas)
            especificaciones.append(especificacion)
        g = Producto(nombre, forma, precio)
        inventario.agregar_producto(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscar(esp)))
    esp_fake = EspecificacionProducto()
    esp_fake.agregar_parametro('bunuelo', 'mediano')
    print(inventario.productos)
    assert len(list(inventario.buscar(esp_fake))) == 0
    g = Producto(nombre, forma, precio)
    inventario.agregar_producto(g)
    try:
        inventario.agregar_producto(g)
        assert False
    except Exception as ex:
        assert ex;

if __name__ == '__main__':
    test_fuzzing_buscar()
