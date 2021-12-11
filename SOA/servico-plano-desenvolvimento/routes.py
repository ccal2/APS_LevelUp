from flask import Blueprint
import json

bp = Blueprint("routes", __name__)

@bp.route("/obter-plano-de-desenvolvimento", methods=["GET"])
def obter_plano_de_desenvolvimento():
    # pega do banco e retorna no json
    return json.dumps({
        "name": "Gabriela"
    })
