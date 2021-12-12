from flask import Blueprint
from controlador import Controlador

bp = Blueprint("routes", __name__)

controlador = Controlador()


@bp.route("/habilidades", methods=["POST"])
def consultar_habiliades():
    return controlador.consultar_habilidades()
