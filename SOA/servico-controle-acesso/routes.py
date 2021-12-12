from flask import Blueprint
from controlador import Controlador

bp = Blueprint("routes", __name__)

controlador = Controlador()


@bp.route("/login", methods=["POST"])
def realizar_login():
    return controlador.realizar_login()
