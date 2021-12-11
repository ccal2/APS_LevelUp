from flask import Blueprint, request
from fachada import Fachada
import json

bp = Blueprint("routes", __name__)

fachada = Fachada()

@bp.route("/listar-habilidades", methods=["GET"])
def consultar_habiliades():
    return json.dumps(fachada.consultar_habilidades())
