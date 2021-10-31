import waitress
from TiendaMascotas.infraestructura.persistenciaPerro import PersistenciaPerro
from TiendaMascotas.infraestructura.persistenciaMascota import PersistenciaMascota
from TiendaMascotas.infraestructura.persistenciaGato import PersistenciaMascota
from TiendaMascotas.infraestructura.persistenciaAve import PersistenciaAve
from TiendaMascotas.infraestructura.persistenciaCamaleon import PersistenciaCamaleon
from TiendaMascotas.infraestructura.persistenciaCuy import PersistenciaCuy

import json
import falcon
from falcon import API


class HolaMundo():

    def on_get(self, req, resp, uuid):
        db = PersistenciaMascota()
        gui = db.load_json(uuid + '.json')
        mensajes = ['Hola Mundo', 'Hola Que hace', 'Adio', 'Ciao', '2+2=4']
        resp.body = json.dumps(gui.__dict__)
        resp.status = falcon.HTTP_OK


def iniciar() -> API:
    # run:app -b 0.0.0.0:2020 --workers 1 -t 240
    api = API()
    api.add_route("/files/{uuid}", HolaMundo())

    return api


app = iniciar()

if __name__ == "__main__":
    waitress.serve(app, port=8081, url_scheme="http")
