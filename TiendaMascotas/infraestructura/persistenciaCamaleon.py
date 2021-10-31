import pickle
import sqlite3
import jsonpickle
from TiendaMascotas.dominio.camaleon import  Camaleon

class PersistenciaCamaleon():

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_pancho.sqlite")
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE CAMALEON(id text primary key, nombre text," \
                    " raza text, tamanio text, precio float," \
                    " edad text, color text, tipoCola text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_camaleon(self, camaleon: Camaleon):
        cursor = self.con.cursor()
        query = "insert into CAMALEON(id , nombre ," \
                " raza , tamanio ,precio ," \
                " edad , color , tipoCola ) values(" \
                f" ?,?,?,?,?,?,?,?,{camaleon.tamanio})"
        cursor.execute(query, (str(camaleon.id), camaleon.nombre, camaleon.raza,
                               camaleon.tamanio, camaleon.precio,camaleon.edad,
                               camaleon.color, camaleon.tipoPlumas))
        self.con.commit()

    @classmethod
    def save_json(cls, camaleon):
        text_open = open("files/" + str(camaleon.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(camaleon)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        camaleon = jsonpickle.decode(json_gui)
        text_open.close()
        return camaleon