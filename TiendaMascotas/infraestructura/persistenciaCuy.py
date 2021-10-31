import pickle
import sqlite3
import jsonpickle
from TiendaMascotas.dominio.cuy import  Cuy

class PersistenciaCuy():

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_pancho.sqlite")
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE AVE(id text primary key, nombre text," \
                    " raza text, tamanio text, precio float," \
                    " edad text, color text, tamanioPelo text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_cuy(self, cuy: Cuy):
        cursor = self.con.cursor()
        query = "insert into AVE(id , nombre ," \
                " raza , tamanio ,precio ," \
                " edad , color , tamanioPelo ) values(" \
                f" ?,?,?,?,?,?,?,?,{cuy.tamanio})"
        cursor.execute(query, (str(cuy.id), cuy.nombre, cuy.raza,
                               cuy.tamanio, cuy.precio, cuy.edad,
                               cuy.color, cuy.tipoPlumas))
        self.con.commit()
    @classmethod
    def save_json(cls, cuy):
        text_open = open("files/" + str(cuy.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(cuy)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        cuy = jsonpickle.decode(json_gui)
        text_open.close()
        return cuy