import pickle
import sqlite3
import jsonpickle
from TiendaMascotas.dominio.perro import Perro

class PersistenciaPerro():
    
    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_pancho.sqlite")
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE PERRO(id text primary key, nombre text," \
                " raza text, tamanio text, precio float," \
                " edad text, color text, tipoPelo text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_perro(self,perro : Perro):
        cursor = self.con.cursor()
        query = "insert into PERRO(id , nombre ," \
                " raza , tamanio ,precio ," \
                " edad , color , tipoPelo ) values(" \
                f" ?,?,?,?,?,?,?,?)"
        cursor.execute(query,(str(perro.id),perro.nombre,perro.raza,
                              perro.tamanio,perro.precio,perro.edad,
                              perro.color,perro.tipoPelo))
        self.con.commit()

    @classmethod
    def save_json(cls, perro):
        text_open = open("files/" + str(perro.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(perro)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        perro = jsonpickle.decode(json_gui)
        text_open.close()
        return perro