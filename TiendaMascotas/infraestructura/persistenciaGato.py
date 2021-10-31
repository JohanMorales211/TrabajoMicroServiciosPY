import pickle
import sqlite3
import jsonpickle
from TiendaMascotas.dominio.gato import Gato


class PersistenciaMascota():

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_pancho.sqlite")
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE GATO(id text primary key, nombre text," \
                    " raza text, tamanio text, precio float," \
                    " edad text, color text, enfermedades text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_gato(self, gato: Gato):
        cursor = self.con.cursor()
        query = "insert into GATO(id , nombre ," \
                " raza , tamanio ,precio ," \
                " edad , color , enfermedades ) values(" \
                f" ?,?,?,?,?,?,?,?,?,{gato.tamanio})"
        cursor.execute(query, (str(gato.id), gato.nombre, gato.raza,
                               gato.tamanio, gato.precio, gato.edad,
                               gato.color, gato.enfermedades))
        self.con.commit()

    @classmethod
    def save_json(cls, gato):
        text_open = open("files/" + str(gato.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(gato)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        gato = jsonpickle.decode(json_gui)
        text_open.close()
        return gato
