import random

from TiendaMascotas.dominio.inventario import Inventario
from TiendaMascotas.dominio.mascota import Mascota
from TiendaMascotas.dominio.especificacionMascota import EspecificacionMascota
from TiendaMascotas.dominio.perro import Perro
from TiendaMascotas.dominio.gato import Gato
from TiendaMascotas.dominio.ave import Ave
from TiendaMascotas.dominio.camaleon import Camaleon
from TiendaMascotas.dominio.cuy import Cuy


def test_buscar():
    razas = ['perro_husky', 'gato_peterbald', 'ave_loro_cacatua', 'reptiles_lagarto_albino', 'cuy']
    colores = {
        'perro_husky': ['blanco', 'blanco y negro', 'cafe y blanco'],
        'gato_peterbald': ['blanco', 'negro', 'gris'],
        'ave_loro_cacatua': ['amarillo', 'rosa', 'amarillo con negro'],
        'reptiles_lagarto_albino': ['blanco', 'rosa'],
        'cuy': ['blanco con cafe', 'cafe', 'negro y blanco']
    }
    inv = Inventario()
    for raza in razas:
        for color in colores[raza]:
            inv.agregar_mascota(Mascota("Javier", raza, 'mediano', 20000, 2, color))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for mascota in inv.buscar(especificacion):
        assert mascota is not None
    assert len(list(inv.buscar(especificacion))) > 0


def test_fuzzing_buscar():
    razas = ['perro_husky', 'gato_peterbald', 'ave_loro_cacatua', 'reptiles_lagarto_albino', 'cuy']
    colores = {
        'perro_husky': ['blanco', 'blanco y negro', 'cafe y blanco'],
        'gato_peterbald': ['blanco', 'negro', 'gris'],
        'ave_loro_cacatua': ['amarillo', 'rosa', 'amarillo con negro'],
        'reptiles_lagarto_albino': ['blanco', 'rosa'],
        'cuy': ['blanco', 'cafe', 'negro y blanco']
    }
    nombres = ['Titino', 'Toby', 'Pancho', 'Polo', 'Ruperta', 'Nieve', 'Copito']
    tamanios = ['pequeño', 'mediano', 'grande']
    precios = [50000, 80000, 150000, 500000, 35000, 5000000]
    edades = [1, 2, 3, 4]
    cantidad_mascotas = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_mascotas):
        raza = random.choice(razas)
        color = random.choice(colores[raza])
        nombre = random.choice(nombres)
        tamanio = random.choice(tamanios)
        precio = random.choice(precios)
        edad = random.choice(edades)
        if i % 10 == 0:
            especificacion = EspecificacionMascota()
            especificacion.agregar_parametro('raza', raza)
            especificacion.agregar_parametro('color', color)
            especificaciones.append(especificacion)
        g = Mascota(raza, color, nombre, tamanio, precio, edad)
        inventario.agregar_mascota(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscar(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscar(esp)))
    esp_fake = EspecificacionMascota()
    esp_fake.agregar_parametro('motiladosMelos', 'ferchoso')
    print(inventario.mascotas)
    assert len(list(inventario.buscar(esp_fake))) == 0
    g = Mascota(raza, color, nombre, tamanio, precio, edad)
    inventario.agregar_mascota(g)
    try:
        inventario.agregar_mascota(g)
        assert False
    except Exception as ex:
        assert ex;


def test_buscar_Perro():
    razas = ['Mestizos', 'Labrador_Retrievers', 'Pastor_Aleman', 'Beagles']
    colores = {
        'Mestizos': ['blanco', 'negro', 'cafe', 'manchado con blanco y negro'],
        'Labrador_Retrievers': ['blanco', 'negro', 'cafe', 'mono'],
        'Pastor_Aleman': ['cafe', 'negro', 'blanco', 'cafe con negro'],
        'Beagles': ['mono con negro', 'blanco con mono', 'mono con negro y blanco']
    }
    inv = Inventario()
    for raza in razas:
        for color in colores[raza]:
            inv.agregar_perro(Perro("Toby", raza, 'promedio normal', 20000, 2, color, "lizo"))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for perro in inv.buscarPerro(especificacion):
        assert perro is not None
    assert len(list(inv.buscarPerro(especificacion))) > 0


def test_fuzzing_buscar_perro():
    razas = ['Mestizos', 'Labrador_Retrievers', 'Pastor_Aleman', 'Beagles']
    colores = {
        'Mestizos': ['blanco', 'negro', 'cafe', 'manchado con blanco y negro'],
        'Labrador_Retrievers': ['blanco', 'negro', 'cafe', 'mono'],
        'Pastor_Aleman': ['cafe', 'negro', 'blanco', 'cafe con negro'],
        'Beagles': ['mono con negro', 'blanco con mono', 'mono con negro y blanco']
    }
    nombres = ['Lufy', 'Polo', 'Garozo', 'Nieve']
    tamanios = ['pequeño', 'mediano', 'grande']
    precios = [50000, 80000, 150000, 500000, 35000, 5000000]
    edades = [1, 2, 3]
    tipo_Pelos = ['lizo', 'rizado', 'raso', 'semi largo']
    cantidad_perros = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_perros):
        raza = random.choice(razas)
        color = random.choice(colores[raza])
        nombre = random.choice(nombres)
        tamanio = random.choice(tamanios)
        precio = random.choice(precios)
        edad = random.choice(edades)
        tipo_Pelo = random.choice(tipo_Pelos)
        if i % 10 == 0:
            especificacion = EspecificacionMascota()
            especificacion.agregar_parametro('raza', raza)
            especificacion.agregar_parametro('color', color)
            especificaciones.append(especificacion)
        g = Perro(nombre, raza, tamanio, precio, edad, color, tipo_Pelo)
        inventario.agregar_perro(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscarPerro(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscarPerro(esp)))
    esp_fake = EspecificacionMascota()
    esp_fake.agregar_parametro('motiladosMelos', 'titinisimo')
    print(inventario.perros)
    assert len(list(inventario.buscarPerro(esp_fake))) == 0
    g = Perro(nombre, raza, tamanio, precio, edad, color, tipo_Pelo)
    inventario.agregar_perro(g)
    try:
        inventario.agregar_perro(g)
        assert False
    except Exception as ex:
        assert ex;


def test_buscar_Gato():
    razas = ['Persa', 'Bengala', 'Siames', 'Esfinge']
    colores = {
        'Persa': ['blanco', 'gris', 'amarillo', 'negro'],
        'Bengala': ['blanco con negro', 'cafe con negro', 'mono con negro', 'gris con blanco y negro'],
        'Siames': ['blanco con negro', 'blanco'],
        'Esfinge': ['piel con negro', 'blanco', 'gris']
    }
    inv = Inventario()
    for raza in razas:
        for color in colores[raza]:
            inv.agregar_gato(Gato("Toby", raza, 'promedio normal', 200000, 1, color, "Conjuntivitis"))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for gato in inv.buscarGato(especificacion):
        assert gato is not None
    assert len(list(inv.buscarGato(especificacion))) > 0

def test_fuzzing_buscar_gato():
    razas = ['Persa', 'Bengala', 'Siames', 'Esfinge']
    colores = {
        'Persa': ['blanco', 'gris', 'amarillo', 'negro'],
        'Bengala': ['blanco con negro', 'cafe con negro', 'mono con negro', 'gris con blanco y negro'],
        'Siames': ['blanco con negro', 'blanco'],
        'Esfinge': ['piel con negro', 'blanco', 'gris']
    }
    nombres = ['Alex', 'Charlie', 'Coco', 'Felix']
    tamanios = ['pequeño', 'mediano', 'grande']
    precios = [1000000, 2000000, 500000, 300000, 2500000]
    edades = [1, 2, 3]
    enfermedades = ['Conjuntivitis', 'Rabia', 'Leucemia felina', 'Panleucopenia felina']
    cantidad_gatos = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_gatos):
        raza = random.choice(razas)
        color = random.choice(colores[raza])
        nombre = random.choice(nombres)
        tamanio = random.choice(tamanios)
        precio = random.choice(precios)
        edad = random.choice(edades)
        enfermedad = random.choice(enfermedades)
        if i % 10 == 0:
            especificacion = EspecificacionMascota()
            especificacion.agregar_parametro('raza', raza)
            especificacion.agregar_parametro('color', color)
            especificaciones.append(especificacion)
        g = Perro(nombre, raza, tamanio, precio, edad, color, enfermedad)
        inventario.agregar_gato(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscarGato(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscarGato(esp)))
    esp_fake = EspecificacionMascota()
    esp_fake.agregar_parametro('motiladosMelos', 'facherisimo')
    print(inventario.gatos)
    assert len(list(inventario.buscarGato(esp_fake))) == 0
    g = Perro(nombre, raza, tamanio, precio, edad, color, enfermedad)
    inventario.agregar_gato(g)
    try:
        inventario.agregar_gato(g)
        assert False
    except Exception as ex:
        assert ex;

def test_buscar_Ave():
    razas = ['Gallina_Domestica', 'Pavo_Domestico', 'Pato_Domestico', 'Ganzo_Domestico']
    colores = {
        'Gallina_Domestica': ['blanco', 'negro', 'cafe'],
        'Pavo_Domestico': ['negro', 'gris', 'cafe', 'blanco con negro'],
        'Pato_Domestico': ['blanco con negro', 'blanco'],
        'Ganzo_Domestico': ['blanco', 'negro con blanco', 'negro con blanco y azul']
    }
    inv = Inventario()
    for raza in razas:
        for color in colores[raza]:
            inv.agregar_ave(Ave("Luriel", raza, 'promedio normal', 100000, 1, color, "Plumas genericas"))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for ave in inv.buscarAve(especificacion):
        assert ave is not None
    assert len(list(inv.buscarAve(especificacion))) > 0

def test_fuzzing_buscar_ave():
    razas = ['Gallina_Domestica', 'Pavo_Domestico', 'Pato_Domestico', 'Ganzo_Domestico']
    colores = {
        'Gallina_Domestica': ['blanco', 'negro', 'cafe'],
        'Pavo_Domestico': ['negro', 'gris', 'cafe', 'blanco con negro'],
        'Pato_Domestico': ['blanco con negro', 'blanco'],
        'Ganzo_Domestico': ['blanco', 'negro con blanco', 'negro con blanco y azul']
    }
    nombres = ['Alita', 'Piquito', 'Plumita', 'Pichi']
    tamanios = ['pequeño', 'mediano', 'grande']
    precios = [1000000, 2000000, 500000, 300000, 2500000]
    edades = [1, 2, 3]
    tipo_Plumas = ['Plumas de vuelo', 'Plumas genéricas']
    cantidad_aves = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_aves):
        raza = random.choice(razas)
        color = random.choice(colores[raza])
        nombre = random.choice(nombres)
        tamanio = random.choice(tamanios)
        precio = random.choice(precios)
        edad = random.choice(edades)
        tipo_Pluma = random.choice(tipo_Plumas)
        if i % 10 == 0:
            especificacion = EspecificacionMascota()
            especificacion.agregar_parametro('raza', raza)
            especificacion.agregar_parametro('color', color)
            especificaciones.append(especificacion)
        g = Ave(nombre, raza, tamanio, precio, edad, color, tipo_Pluma)
        inventario.agregar_ave(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscarAve(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscarAve(esp)))
    esp_fake = EspecificacionMascota()
    esp_fake.agregar_parametro('lengua', 'morada')
    print(inventario.aves)
    assert len(list(inventario.buscarAve(esp_fake))) == 0
    g = Ave(nombre, raza, tamanio, precio, edad, color, tipo_Pluma)
    inventario.agregar_ave(g)
    try:
        inventario.agregar_ave(g)
        assert False
    except Exception as ex:
        assert ex;

def test_buscar_Camaleon():
    razas = ['Enano_de_Smith', 'Parson', 'Jackson', 'Pantera']
    colores = {
        'Enano_de_Smith': ['cafe', 'blanco', 'piedra negra'],
        'Parson': ['rojo con negro', 'verde con azul', 'gris'],
        'Jackson': ['verde', 'amarillo con verde claro'],
        'Pantera': ['morado con azul y verde', 'rojo con blanco y lineas gris', 'verde con amarillo y rojo']
    }
    inv = Inventario()
    for raza in razas:
        for color in colores[raza]:
            inv.agregar_camaleon(Camaleon("Jaceiro", raza, 'promedio normal', 300000, 1, color, "Normal"))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for camaleon in inv.buscarCamaleon(especificacion):
        assert camaleon is not None
    assert len(list(inv.buscarCamaleon(especificacion))) > 0

def test_fuzzing_buscar_camaleon():
    razas = ['Enano_de_Smith', 'Parson', 'Jackson', 'Pantera']
    colores = {
        'Enano_de_Smith': ['cafe', 'blanco', 'piedra negra'],
        'Parson': ['rojo con negro', 'verde con azul', 'gris'],
        'Jackson': ['verde', 'amarillo con verde claro'],
        'Pantera': ['morado con azul y verde', 'rojo con blanco y lineas gris', 'verde con amarillo y rojo']
    }
    nombres = ['Hulk', 'Hidra', 'Gigante', 'Atlas']
    tamanios = ['pequeño', 'mediano', 'grande']
    precios = [1000000, 2000000, 500000, 300000, 2500000]
    edades = [1, 2, 3]
    tipo_Colas = ['Palo lizo', 'Con puntas']
    cantidad_camaleones = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_camaleones):
        raza = random.choice(razas)
        color = random.choice(colores[raza])
        nombre = random.choice(nombres)
        tamanio = random.choice(tamanios)
        precio = random.choice(precios)
        edad = random.choice(edades)
        tipo_Cola = random.choice(tipo_Colas)
        if i % 10 == 0:
            especificacion = EspecificacionMascota()
            especificacion.agregar_parametro('raza', raza)
            especificacion.agregar_parametro('color', color)
            especificaciones.append(especificacion)
        g = Camaleon(nombre, raza, tamanio, precio, edad, color, tipo_Cola)
        inventario.agregar_camaleon(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscarCamaleon(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscarCamaleon(esp)))
    esp_fake = EspecificacionMascota()
    esp_fake.agregar_parametro('lengua', 'amarilla')
    print(inventario.camaleones)
    assert len(list(inventario.buscarCamaleon(esp_fake))) == 0
    g = Camaleon(nombre, raza, tamanio, precio, edad, color, tipo_Cola)
    inventario.agregar_camaleon(g)
    try:
        inventario.agregar_camaleon(g)
        assert False
    except Exception as ex:
        assert ex;

def test_buscar_Cuy():
    razas = ['Americano', 'Abisino', 'Peruano', 'Coronet']
    colores = {
        'Americano': ['amarillo con blanco', 'negro con blanco y gris', 'cafe'],
        'Abisino': ['cafe', 'blanco con negro y cafe', 'cafe amarilloso'],
        'Peruano': ['gris', 'cafe'],
        'Coronet': ['gris con blanco', 'cafe con blanco', 'blanco con negro']
    }
    inv = Inventario()
    for raza in razas:
        for color in colores[raza]:
            inv.agregar_cuy(Cuy("Jaceiro", raza, 'promedio normal', 300000, 1, color, "Normal"))
    especificacion = EspecificacionMascota()
    especificacion.agregar_parametro('raza', raza)
    for cuy in inv.buscarCuy(especificacion):
        assert cuy is not None
    assert len(list(inv.buscarCuy(especificacion))) > 0

def test_fuzzing_buscar_cuy():
    razas = ['Americano', 'Abisino', 'Peruano', 'Coronet']
    colores = {
        'Americano': ['amarillo con blanco', 'negro con blanco y gris', 'cafe'],
        'Abisino': ['cafe', 'blanco con negro y cafe', 'cafe amarilloso'],
        'Peruano': ['gris', 'cafe'],
        'Coronet': ['gris con blanco', 'cafe con blanco', 'blanco con negro']
    }
    nombres = ['Black', 'Negrito', 'Brownie', 'Atlas']
    tamanios = ['pequeño', 'mediano', 'grande']
    precios = [1000000, 2000000, 500000, 300000, 2500000]
    edades = [1, 2, 3]
    tamanioPelos = ['Corto', 'Largo']
    cantidad_camaleones = random.randint(100, 1000)
    inventario = Inventario()
    especificaciones = []
    for i in range(cantidad_camaleones):
        raza = random.choice(razas)
        color = random.choice(colores[raza])
        nombre = random.choice(nombres)
        tamanio = random.choice(tamanios)
        precio = random.choice(precios)
        edad = random.choice(edades)
        tamanioPelo = random.choice(tamanioPelos)
        if i % 10 == 0:
            especificacion = EspecificacionMascota()
            especificacion.agregar_parametro('raza', raza)
            especificacion.agregar_parametro('color', color)
            especificaciones.append(especificacion)
        g = Cuy(nombre, raza, tamanio, precio, edad, color, tamanioPelo)
        inventario.agregar_cuy(g)
    cantidad_busquedas = random.randint(1, len(especificaciones))
    for i in range(cantidad_busquedas):
        esp = random.choice(especificaciones)
        assert len(list(inventario.buscarCuy(esp))) >= 0
        print('encontradas:')
        print(list(inventario.buscarCuy(esp)))
    esp_fake = EspecificacionMascota()
    esp_fake.agregar_parametro('cagar', 'circulo')
    print(inventario.cuyes)
    assert len(list(inventario.buscarCuy(esp_fake))) == 0
    g = Cuy(nombre, raza, tamanio, precio, edad, color, tamanioPelo)
    inventario.agregar_cuy(g)
    try:
        inventario.agregar_cuy(g)
        assert False
    except Exception as ex:
        assert ex;

if __name__ == '__main__':
    test_fuzzing_buscar()
