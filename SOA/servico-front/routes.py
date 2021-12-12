from flask import Blueprint, render_template, redirect, url_for

from controles.tela_habilidades import TelaHabilidadesControle

bp = Blueprint("routes", __name__)

controle_tela_habilidades = TelaHabilidadesControle()

@bp.route("/", methods=["GET"])
def tela_redirecionamento_inicial():
    return redirect(url_for("routes.tela_login_usuario_controle"))


@bp.route("/login", methods=["GET", "POST"])
def tela_login_usuario_controle():
    # erro = None
    # if request.method == "POST":
    #     resultado = controleLoginUsuario.realizar_login(request.form["email"], request.form["senha"])
    #     erro = resultado["erro"]    
    #     if erro is None:
    #         return redirect("/inicio")
    # return render_template(controleLoginUsuario.tela, erro=erro)
    return render_template("TelaLoginUsuario.html")


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
