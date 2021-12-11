from flask import Blueprint
import json

bp = Blueprint("routes", __name__)

@bp.route("/listar-habilidades", methods=["GET"])
def consultar_habiliades():
    # pega do banco e retorna no json
    return json.dumps({
        "name": "Gabriela"
    })
