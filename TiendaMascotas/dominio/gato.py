import uuid

from TiendaMascotas.dominio.mascota import Mascota


class Gato(Mascota):

    def __init__(self, nombre, raza, tamanio, precio, edad, color, enfermedades, *args, **kargs):
        self.nombre = nombre
        self.raza = raza
        self.tamanio = tamanio
        self.precio = precio
        self.edad = edad
        self.color = color
        self.enfermedades = enfermedades
        self.id = str(uuid.uuid4())
        super().__init__(nombre, raza, tamanio, precio, edad, color)

    def __str__(self):
        return f"{self.nombre}---{self.raza}---{self.tamanio}---{self.precio}---{self.edad}---" \
               f"{self.color}---{self.enfermedades}---{self.id}"

    def __repr__(self):
        return str(self.id)

    def cumpleGato(self, especificacion):
        dict_gato = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_gato or dict_gato[k] != especificacion.get_value(k):
                return False
        return True