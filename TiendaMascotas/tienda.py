import os

from TiendaMascotas.dominio.inventario import Inventario
from TiendaMascotas.dominio.perro import Perro
from TiendaMascotas.dominio.gato import Gato
from TiendaMascotas.dominio.ave import Ave
from TiendaMascotas.dominio.camaleon import Camaleon
from TiendaMascotas.dominio.cuy import Cuy
from TiendaMascotas.infraestructura.persistenciaPerro import PersistenciaPerro
from TiendaMascotas.infraestructura.persistenciaGato import PersistenciaMascota
from TiendaMascotas.infraestructura.persistenciaAve import PersistenciaAve
from TiendaMascotas.infraestructura.persistenciaCamaleon import PersistenciaCamaleon
from TiendaMascotas.infraestructura.persistenciaCuy import PersistenciaCuy
from TiendaMascotas.infraestructura.persistenciaMascota import PersistenciaMascota
import random

inventario = Inventario()

if __name__ == '__main__':

    saverPerro = PersistenciaPerro()
    saverGatos = PersistenciaMascota()
    saverAves = PersistenciaAve()
    saverCamaleon = PersistenciaCamaleon()
    saverCuy = PersistenciaCuy()

    menuPrincipal = True
    subMenu = True
    while menuPrincipal:

        menuPrincipal = int(input("Eliga lo que quiera hacer en el menú: \n"
                                  "1. Agregar mascota \n"
                                  "2. Salir \n"
                                  "Por favor ingrese una opcion del menú: "))

        if menuPrincipal == 1:
            while subMenu:
                if subMenu == 1:
                    subMenu = int(input("Eliga el animal que desea agregar: \n"
                                        "1. Perro \n"
                                        "2. Gato \n"
                                        "3. Ave \n"
                                        "4. Camaleon \n"
                                        "5. Cuy \n"
                                        "6. Volver al menú principal "))

                    if subMenu == 1:
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
                        raza = random.choice(razas)
                        color = random.choice(colores[raza])
                        nombre = random.choice(nombres)
                        tamanio = random.choice(tamanios)
                        precio = random.choice(precios)
                        edad = random.choice(edades)
                        tipo_Pelo = random.choice(tipo_Pelos)
                        g = Perro(nombre, raza, tamanio, precio, edad, color, tipo_Pelo)
                        inventario = Inventario()
                        inventario_json = Inventario()

                        menuGuardarPrimero = int(input("Eliga en que manera desea guardar: \n"
                                  "1. Agregar en save_json_perro \n"
                                  "2. Agregar en base de datos \n"
                                  "3. Volver al menú \n"
                                    "Por favor ingrese una opcion del menú: "))

                        if menuGuardarPrimero == 1:
                            PersistenciaMascota.save_json(g)
                            for file in os.listdir("./files"):
                                if '.json' in file:
                                    inventario_json.agregar_perro(PersistenciaMascota.load_json(file))
                            for g in inventario.perros:
                                PersistenciaMascota.save_json(g)
                                print("La mascota ha sido añadida con exito")
                                print(subMenu)

                        elif menuGuardarPrimero == 2:
                            saverPerro.guardar_perro(g)
                            print("La mascota ha sido añadida con exito")
                            print(subMenu)

                        elif menuGuardarPrimero == 3:
                            print(menuPrincipal)

                        else:
                            print("Por favor ingrese bien los numeros")
                            print(menuGuardarPrimero)
                            break

                if subMenu == 2:
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
                    g = Gato(nombres, razas, tamanios, precios,edades, colores,enfermedades)
                    inventario = Inventario()
                    inventario_json = Inventario()

                    menuGuardarSegundo = int(input("Eliga en que manera desea guardar: \n"
                                                   "1. Agregar en save_json \n"
                                                   "2. Agregar en base de datos \n"
                                                   "3. Volver al menú \n"
                                                   "Por favor ingrese una opcion del menú: "))
                    if (menuGuardarSegundo == 1):
                        PersistenciaMascota.save_json(g)
                        for file in os.listdir("./files"):
                            if '.json' in file:
                                inventario_json.agregar_gato(PersistenciaMascota.load_json(file))
                        for g in inventario.gatos:
                            PersistenciaMascota.save_json(g)
                        print("La mascota ha siso guardada con exito")
                        print(subMenu)

                    elif (menuGuardarSegundo == 2):
                        saverGatos.guardar_gato(g)
                        print("La mascota ha siso guardada con exito")
                        print(subMenu)

                    elif (menuGuardarSegundo == 3):
                        print(subMenu)

                    else:
                        print("Por favor ingrese solo los numeros que pide el menu")
                        print(menuGuardarSegundo)
                        break

                if subMenu == 3:
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
                    g = Ave(nombres,razas,tamanios,precios,edades,colores,tipo_Plumas)
                    inventario = Inventario()
                    inventario_json = Inventario()

                    menuGuardarTercero = int(input("Eliga en que manera desea guardar: \n"
                                                   "1. Agregar en save_json \n"
                                                   "2. Agregar en base de datos \n"
                                                   "3. Volver al menú \n"
                                                   "Por favor ingrese una opcion del menú: "))

                    if (menuGuardarTercero == 1):
                        PersistenciaMascota.save_json(g)
                        for file in os.listdir("./files"):
                            if '.json' in file:
                                inventario_json.agregar_ave(PersistenciaMascota.load_json(file))
                        for g in inventario.aves:
                            PersistenciaMascota.save_json(g)
                        print("La mascota ha siso guardada con exito")
                        print(subMenu)


                    elif (menuGuardarTercero == 2):
                        saverAves.guardar_ave(g)
                        print("La mascota ha siso guardada con exito")
                        print(subMenu)

                    elif (menuGuardarTercero == 3):
                        print(subMenu)

                    else:
                        print("Por favor ingrese solo los numeros que pide el menu")
                        print(menuGuardarTercero)
                        break

                if subMenu == 4:
                    razas = ['Enano_de_Smith', 'Parson', 'Jackson', 'Pantera']
                    colores = {
                        'Enano_de_Smith': ['cafe', 'blanco', 'piedra negra'],
                        'Parson': ['rojo con negro', 'verde con azul', 'gris'],
                        'Jackson': ['verde', 'amarillo con verde claro'],
                        'Pantera': ['morado con azul y verde', 'rojo con blanco y lineas gris',
                                    'verde con amarillo y rojo']
                    }
                    nombres = ['Hulk', 'Hidra', 'Gigante', 'Atlas']
                    tamanios = ['pequeño', 'mediano', 'grande']
                    precios = [1000000, 2000000, 500000, 300000, 2500000]
                    edades = [1, 2, 3]
                    tipo_Colas = ['Palo lizo', 'Con puntas']
                    g = Camaleon(nombres,razas,tamanios,precios,edades,colores,tipo_Colas)
                    inventario = Inventario()
                    inventario_json = Inventario()

                    menuGuardarCuarto = int(input("Eliga en que manera desea guardar: \n"
                                                   "1. Agregar en save_json \n"
                                                   "2. Agregar en base de datos \n"
                                                   "3. Volver al menú \n"
                                                   "Por favor ingrese una opcion del menú: "))
                    if (menuGuardarCuarto == 1):
                        PersistenciaMascota.save_json(g)
                        for file in os.listdir("./files"):
                            if '.json' in file:
                                inventario_json.agregar_camaleon(PersistenciaMascota.load_json(file))
                        for g in inventario.camaleones:
                            PersistenciaMascota.save_json(g)
                        print("La mascota ha siso guardada con exito")
                        print(subMenu)


                    elif (menuGuardarCuarto == 2):
                        saverCamaleon.guardar_camaleon(g)
                        print("La mascota ha siso guardada con exito")
                        print(subMenu)

                    elif (menuGuardarCuarto == 3):
                        print(subMenu)

                    else:
                        print("Por favor ingrese solo los numeros que pide el menu")
                        print(menuGuardarCuarto)
                        break

                if subMenu == 5:
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
                    g = Cuy(nombres,razas,tamanios,precios,edades,colores,tamanioPelos)
                    inventario = Inventario()
                    inventario_json = Inventario()

                    menuGuardarQuinto = int(input("Eliga en que manera desea guardar: \n"
                                                  "1. Agregar en save_json \n"
                                                  "2. Agregar en base de datos \n"
                                                  "3. Volver al menú \n"
                                                  "Por favor ingrese una opcion del menú: "))
                    if (menuGuardarQuinto == 1):
                        PersistenciaMascota.save_json(g)
                        for file in os.listdir("./files"):
                            if '.json' in file:
                                inventario_json.agregar_cuy(PersistenciaMascota.load_json(file))
                        for g in inventario.camaleones:
                            PersistenciaMascota.save_json(g)
                        print("La mascota ha siso guardada con exito")
                        print(subMenu)


                    elif (menuGuardarQuinto == 2):
                        saverCamaleon.guardar_camaleon(g)
                        print("La mascota ha siso guardada co n exito")
                        print(subMenu)

                    elif (menuGuardarQuinto == 3):
                        print(subMenu)

                    else:
                        print("Por favor ingrese solo los numeros que pide el menu")
                        print(menuGuardarQuinto)
                        break

                if subMenu == 6:
                    subMenu = False

        elif menuPrincipal == 2:
            print("Gracias por visitar la tienda!")

        else:
            print("por favor ingrese los numeros del menu")
            break