from flask import Blueprint
from fachada import Fachada

bp = Blueprint("routes", __name__)

fachada = Fachada()

@bp.route("/plano-de-desenvolvimento/<id>", methods=["GET"])
def obter_plano_de_desenvolvimento(id):
    return fachada.obter_plano_de_desenvolvimento(id)
