import uuid

class Mascota:

    def __init__(self, nombre, raza, tamanio, precio, edad, color,*args, **kargs):
        self.nombre = nombre
        self.raza = raza
        self.tamanio = tamanio
        self.precio = precio
        self.edad = edad
        self.color = color
        self.id = str(uuid.uuid4())

    def __str__(self):
        return f"{self.nombre}---{self.raza}---{self.tamanio}---{self.precio}---{self.edad}---{self.color}---{self.id}"

    def __repr__(self):
        return str(self.id)

    def cumple(self, especificacion):
        dict_mascota = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_mascota or dict_mascota[k] != especificacion.get_value(k):
                return False
        return True
