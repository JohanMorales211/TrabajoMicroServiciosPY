import pickle
import sqlite3
import jsonpickle
from TiendaMascotas.dominio.ave import Ave

class PersistenciaAve():

    def connect(self):
        self.con = sqlite3.connect("la_tienda_de_pancho.sqlite")
        self.__crear_tabla()

    def __crear_tabla(self):
        try:
            cursor = self.con.cursor()
            query = "CREATE TABLE AVE(id text primary key, nombre text," \
                    " raza text, tamanio text, precio float," \
                    " edad text, color text, tipoPlumas text) "
            cursor.execute(query)
        except sqlite3.OperationalError as ex:
            pass

    def guardar_ave(self, ave: Ave):
        cursor = self.con.cursor()
        query = "insert into AVE(id , nombre ," \
                " raza , tamanio ,precio ," \
                " edad , color , tipoPlumas ) values(" \
                f" ?,?,?,?,?,?,?,?,{ave.tamanio})"
        cursor.execute(query, (str(ave.id), ave.nombre, ave.raza,
                               ave.tamanio, ave.precio,ave.edad,
                               ave.color, ave.tipoPlumas))
        self.con.commit()

    @classmethod
    def save_json(cls, ave):
        text_open = open("files/" + str(ave.id) + '.json', mode='w')
        json_gui = jsonpickle.encode(ave)
        text_open.write(json_gui)
        text_open.close()

    @classmethod
    def load_json(cls, file_name):
        text_open = open("files/" + file_name, mode='r')
        json_gui = text_open.readline()
        ave = jsonpickle.decode(json_gui)
        text_open.close()
        return ave