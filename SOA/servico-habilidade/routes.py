from flask import Blueprint, request
from fachada import Fachada

bp = Blueprint("routes", __name__)

fachada = Fachada()

@bp.route("/habilidades", methods=["POST"])
def consultar_habiliades():
    return fachada.consultar_habilidades()
