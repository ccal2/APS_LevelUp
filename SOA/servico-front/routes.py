from flask import Blueprint, render_template, redirect, url_for, request

from controles.controle_tela_login import ControleTelaLogin
from controles.controle_tela_habilidades import ControleTelaHabilidades

bp = Blueprint("routes", __name__)

controle_tela_login = ControleTelaLogin()
controle_tela_habilidades = ControleTelaHabilidades()

@bp.route("/", methods=["GET"])
def tela_redirecionamento_inicial():
    return redirect(url_for("routes.tela_login_usuario_controle"))


@bp.route("/login", methods=["GET", "POST"])
def tela_login_usuario_controle():
    erro = None
    if request.method == "POST":
        resultado = controle_tela_login.realizar_login()
        erro = resultado.get("erro")
    return render_template("TelaLoginUsuario.html", erro=erro)


@bp.route("/inicio", methods=["GET"])
def tela_inicio_controle():
    return render_template("TelaInicio.html")


@bp.route("/habilidades", methods=["GET"])
def tela_habilidades():
    resultado = controle_tela_habilidades.consultar_habilidades()
    erro = resultado.get("erro")
    habilidades =  resultado.get("habilidades")
    return render_template("TelaHabilidades.html", erro=erro, habilidades=habilidades)


# @bp.route("/recomendacoes/", methods=["GET"])
# def tela_recomendacoes_do_sistema_controle():
#     resultado = controleRecomendacoes.solicitar_recomendacoes()
#     erro = resultado["erro"]
#     habilidades = resultado["recomendacoes"]
#     return render_template("TelaRecomendacoesDoSistema.html", erro=erro, habilidades=habilidades)
