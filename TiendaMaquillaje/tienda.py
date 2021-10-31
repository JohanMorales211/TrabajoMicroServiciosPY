import os
import random
from TiendaMaquillaje.dominio.inventario import Inventario
from TiendaMaquillaje.dominio.producto import Producto
from TiendaMaquillaje.infraestructura.persistenciaProducto import PersistenciaProducto

inventario = Inventario()

if __name__ == '__main__':
    categoriaProductosTienda = ['líquida', 'polvo', 'crema',
                                'aceite']
    colores = {
        'líquida': ['fucsia', 'rojo', 'vino tinto', 'palo de rosa', 'cereza'],
        'polvo': ['piel', 'canela', 'piel morena', 'tradicional'],
        'crema': ['blanca', 'dorado', 'palo de rosa'],
        'aceite': ['neutro']
    }
    marcas = ['Loreal', 'Celine', 'Rimowa', 'Fendi', 'Essie', 'Diesel', 'Redken']
    nombres = ['labial', 'delineador_Ojos', 'polvo_Compacto', 'delineador_Cejas', 'corrector_Ojos', 'paleta_De_Sombras']
    precios = [50000, 80000, 150000, 200000, 55000, 120000]
    cantidad_productos = random.randint(100, 1000)
    categoriaProducto = random.choice(categoriaProductosTienda)
    color = random.choice(colores[categoriaProducto])
    marca = random.choice(marcas)
    nombre = random.choice(nombres)
    precio = random.choice(precios)
    g = Producto(nombre,categoriaProducto,color,marca,precio)
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