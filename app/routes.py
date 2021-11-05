from flask import Blueprint, render_template

from model.usuario.colaborador.repositorio_colaborador_firestore import RepositorioColaboradorFirestore

bp = Blueprint("routes", __name__)

@bp.route("/consultar", methods=["GET"])
def consultar():
    repo = RepositorioColaboradorFirestore()

    colaborador = repo.consultar_colaborador(email="ccal2@cin.ufpe.br")

    return render_template("consulta_colaborador.html", colaborador=colaborador)

@bp.route("/inicio/colaborador", methods=["GET"])
def inicio_colaborador():
    return render_template("inicio_colaborador.html")

@bp.route("/inicio/administrador", methods=["GET"])
def inicio_administrador():
    return render_template("inicio_administrador.html")

@bp.route("/recomendacoes/colaborador", methods=["GET"])
def recomendacoes_colaborador():
    # precisa chamar o metodo que vai pegar o usuario logado e gerar as recomendacoes
    # depois passar pro template
    return render_template("recomendacoes_sistema.html")
