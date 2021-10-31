import uuid

class Producto:
    def __init__(self, nombre, categoria, color, marca, precio, *args, **kargs):
        self.nombre = nombre
        self.categoria = categoria
        self.color = color
        self.marca = marca
        self.precio = precio
        self.id = uuid.uuid4()

    def __str__(self):
        return f"{self.nombre}---{self.categoria}---{self.color}---{self.marca}---{self.precio}---{self.id}"

    def __repr__(self):
        return str(self.id)

    def cumple(self, especificacion):
        dict_producto = self.__dict__
        for k in especificacion.get_keys():
            if k not in dict_producto or dict_producto[k] != especificacion.get_value(k):
                return False
        return True