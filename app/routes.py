from flask import Blueprint, render_template

from model.usuario.colaborador.RepositorioColaboradorFirestore import RepositorioColaboradorFirestore

bp = Blueprint("routes", __name__)

@bp.route("/consultar", methods=["GET"])
def consultar():
    repo = RepositorioColaboradorFirestore()

    colaborador = repo.consultar_colaborador(email="ccal2@cin.ufpe.br")

    return render_template("consulta_colaborador.html", colaborador=colaborador)
