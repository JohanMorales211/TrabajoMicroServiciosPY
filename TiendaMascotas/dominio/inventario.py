from TiendaMascotas.dominio.especificacionMascota import EspecificacionMascota
from TiendaMascotas.dominio.mascota import Mascota
from TiendaMascotas.dominio.perro import Perro
from TiendaMascotas.dominio.gato import Gato
from TiendaMascotas.dominio.ave import Ave
from TiendaMascotas.dominio.camaleon import Camaleon
from TiendaMascotas.dominio.cuy import Cuy

class Inventario:

    def __init__(self):
        self.mascotas = []
        self.perros = []
        self.gatos = []
        self.aves = []
        self.camaleones = []
        self.cuyes = []

    def agregar_mascota(self, mascota):
        if type(mascota) == Mascota:
            espec = EspecificacionMascota()
            espec.agregar_parametro('id', mascota.id)
            if len(list(self.buscar(espec))) == 0:
                self.mascotas.append(mascota)
            else:
                raise Exception('Mascota repetida')

    def buscar(self,especificacion):
        for g in self.mascotas:
            if g.cumple(especificacion):
                yield g

    def agregar_perro(self, perro):
        if type(perro) == Perro:
            espec = EspecificacionMascota()
            espec.agregar_parametro('id', perro.id)
            if len(list(self.buscarPerro(espec))) == 0:
                self.perros.append(perro)
            else:
                raise Exception('Perro repetido')

    def buscarPerro(self,especificacion):
        for g in self.perros:
            if g.cumplePerro(especificacion):
                yield g

    def agregar_gato(self, gato):
        if type(gato) == Gato:
            espec = EspecificacionMascota()
            espec.agregar_parametro('id', gato.id)
            if len(list(self.buscarGato(espec))) == 0:
                self.gatos.append(gato)
            else:
                raise Exception('Gato repetido')

    def buscarGato(self,especificacion):
        for g in self.gatos:
            if g.cumpleGato(especificacion):
                yield g

    def agregar_ave(self, ave):
        if type(ave) == Ave:
            espec = EspecificacionMascota()
            espec.agregar_parametro('id', ave.id)
            if len(list(self.buscarAve(espec))) == 0:
                self.aves.append(ave)
            else:
                raise Exception('Ave repetida')

    def buscarAve(self,especificacion):
        for g in self.aves:
            if g.cumpleAve(especificacion):
                yield g

    def agregar_camaleon(self, camaleon):
        if type(camaleon) == Camaleon:
            espec = EspecificacionMascota()
            espec.agregar_parametro('id', camaleon.id)
            if len(list(self.buscarCamaleon(espec))) == 0:
                self.camaleones.append(camaleon)
            else:
                raise Exception('Camaleon repetido')

    def buscarCamaleon(self, especificacion):
        for g in self.camaleones:
            if g.cumpleCamaleon(especificacion):
                yield g

    def agregar_cuy(self, cuy):
        if type(cuy) == Cuy:
            espec = EspecificacionMascota()
            espec.agregar_parametro('id', cuy.id)
            if len(list(self.buscarCuy(espec))) == 0:
                self.cuyes.append(cuy)
            else:
                raise Exception('Cuy repetido')

    def buscarCuy(self, especificacion):
        for g in self.cuyes:
            if g.cumpleRuedor(especificacion):
                yield g