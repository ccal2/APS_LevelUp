from flask import Blueprint, request
from controlador import Controlador

bp = Blueprint("routes", __name__)

controlador = Controlador()

@bp.route("/habilidades", methods=["POST"])
def consultar_habiliades():
    ...

@bp.route("/plano-de-desenvolvimento/<id>", methods=["GET"])
def obter_plano_de_desenvolvimento(id):
    ...

@bp.route("/login", methods=["POST"])
def realizar_login():
    ...