from flask import Blueprint, render_template, redirect, request

from controles.tela_login_usuario_controle import TelaLoginUsuarioControle
from controles.tela_recomendacoes_do_sistema_controle import TelaRecomendacoesDoSistemaControle

# Usado para pegar o colaborador já logado (pré-condição do caso de uso implementado)
from model.colaborador.repositorio_colaborador_firestore import RepositorioColaboradorFirestore

bp = Blueprint("routes", __name__)


@bp.route("/inicio", methods=["GET"])
def tela_inicio_controle():
    return render_template("TelaInicio.html")


@bp.route("/recomendacoes/", methods=["GET"])
def tela_recomendacoes_do_sistema_controle():
    controle = TelaRecomendacoesDoSistemaControle()
    habilidades = controle.solicitar_recomendacoes()
    return render_template("TelaRecomendacoesDoSistema.html", habilidades=habilidades)


@bp.route("/login", methods=["GET", "POST"])
def tela_login_usuario_controle():
    controle = TelaLoginUsuarioControle()
    erro = None
    if request.method == "POST":
        resultado = controle.realizar_login(request.form["email"], request.form["senha"])
        if resultado["status"] == "erro":
            erro = resultado["mensagem"]
        elif resultado["status"] == "sucesso":
            return redirect("/inicio")
    return render_template(controle.tela, erro=erro)
