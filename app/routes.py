from flask import Blueprint, render_template, redirect, request

from controles.tela_login_usuario_controle import TelaLoginUsuarioControle
from controles.tela_recomendacoes_do_sistema_controle import TelaRecomendacoesDoSistemaControle

# Usado para pegar o colaborador já logado (pré-condição do caso de uso implementado)
from model.usuario.colaborador.repositorio_colaborador_firestore import RepositorioColaboradorFirestore

bp = Blueprint("routes", __name__)


@bp.route("/inicio/colaborador", methods=["GET"])
def tela_inicio_colaborador_controle():
    return render_template("TelaInicioColaborador.html")


@bp.route("/inicio/administrador", methods=["GET"])
def tela_inicio_administrador_controle():
    return render_template("TelaInicioAdministrador.html")


@bp.route("/recomendacoes/colaborador/<email_colaborador>", methods=["GET"])
def tela_recomendacoes_do_sistema_controle(email_colaborador):
    # Pegar colaborador já logado (pré-condição do caso de uso)
    repositorio_colaborador = RepositorioColaboradorFirestore()
    colaborador = repositorio_colaborador.consultar_colaborador(email_colaborador)
    if colaborador is None:
        return "Colaborador não encontrado"

    controle = TelaRecomendacoesDoSistemaControle()
    habilidades = controle.solicitar_recomendacoes(colaborador)
    return render_template("TelaRecomendacoesDoSistema.html", habilidades=habilidades)


@bp.route("/login", methods=["GET", "POST"])
def tela_login_usuario_controle():
    controle = TelaLoginUsuarioControle()
    error = None
    if request.method == "POST":
        resultado = controle.realizar_login(request.form["email"], request.form["password"])
        if "erro" in resultado.keys():
            error = resultado["erro"]
        if "redirecionar" in resultado.keys():
            return redirect(resultado["redirecionar"])
    return render_template(controle.tela, error=error)
