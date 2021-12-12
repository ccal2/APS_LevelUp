from flask import Blueprint
from controlador import Controlador

bp = Blueprint("routes", __name__)

controlador = Controlador()

@bp.route("/plano-de-desenvolvimento/<id>", methods=["GET"])
def obter_plano_de_desenvolvimento(id):
    return controlador.obter_plano_de_desenvolvimento(id)
