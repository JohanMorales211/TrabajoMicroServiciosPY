import random
from TiendaMaquillaje.dominio.inventario import Inventario
from TiendaMaquillaje.dominio.producto import Producto
from TiendaMaquillaje.dominio.especificacionProducto import EspecificacionProducto


def test_buscar():
    categoriaProductosTienda = ['líquida', 'polvo', 'crema',
                       'aceite']
    colores = {
        'líquida': ['fucsia', 'rojo', 'vino tinto', 'palo de rosa', 'cereza'],
        'polvo': ['piel', 'canela', 'piel morena', 'tradicional'],
        'crema': ['blanca', 'dorado','palo de rosa'],
        'aceite': ['neutro']
    }
    inv = Inventario()
    for categoriaProductoTienda in categoriaProductosTienda:
        for color in colores[categoriaProductoTienda]:
            inv.agregar_producto(Producto("ojos", "polvo", color, "Vogue",50000))
    especificacion = EspecificacionProducto()
    especificacion.agregar_parametro('nombreProductoTienda', categoriaProductoTienda)
    for producto in inv.buscar(especificacion):
        assert producto is not None
    assert len(list(inv.buscar(especificacion))) >= 0

def test_fuzzing_buscar():
    categoriaProductosTienda = ['liquida', 'polvo', 'crema',
                                'aceite']
    colores = {
        'liquida': ['fucsia', 'rojo', 'vino tinto', 'palo de rosa', 'cereza'],
        'polvo': ['piel', 'canela', 'piel morena', 'tradicional'],
        'crema': ['blanca', 'dorado', 'palo de rosa'],
        'aceite': ['neutro']
    }
    marcas = ['Loreal', 'Celine', 'Rimowa', 'Fendi', 'Essie', 'Diesel', 'Redken']
    nombres = ['labial', 'delineador_Ojos', 'polvo_Compacto', 'delineador_Cejas', 'corrector_Ojos', 'paleta_De_Sombras']
    precios = [50000, 80000, 150000, 200000, 55000, 120000]
    cantidad_productos = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_productos):
        categoriaProducto = random.choice(categoriaProductosTienda)
        color = random.choice(colores[categoriaProducto])
        marca = random.choice(marcas)
        nombre = random.choice(nombres)
        precio = random.choice(precios)
        if i % 10 == 0:
            especificacion = EspecificacionProducto()
            especificacion.agregar_parametro('categoria', categoriaProducto)
            especificacion.agregar_parametro('color', color)
            especificaciones.append(especificacion)
        g = Producto(nombre,categoriaProducto,color,marca,precio)
        inventario.agregar_producto(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscar(esp)))
    esp_fake = EspecificacionProducto()
    esp_fake.agregar_parametro('locion', 'fresa',40000)
    print(inventario.productos)
    assert len(list(inventario.buscar(esp_fake))) == 0
    g = Producto(nombre,categoriaProducto,color,marca,precio)
    inventario.agregar_producto(g)
    try:
        inventario.agregar_producto(g)
        assert False
    except Exception as ex:
        assert ex;

if __name__ == '__main__':
    test_fuzzing_buscar()