from flask import Blueprint, render_template, redirect, request

# from controles.tela_login_usuario_controle import TelaLoginUsuarioControle
# from controles.tela_recomendacoes_do_sistema_controle import TelaRecomendacoesDoSistemaControle

bp = Blueprint("routes", __name__)


# controleRecomendacoes = TelaRecomendacoesDoSistemaControle()
# controleLoginUsuario = TelaLoginUsuarioControle()


# @bp.route("/inicio", methods=["GET"])
# def tela_inicio_controle():
#     return render_template("TelaInicio.html")


# @bp.route("/recomendacoes/", methods=["GET"])
# def tela_recomendacoes_do_sistema_controle():
#     erro = None
#     habilidades = None
#     resultado = controleRecomendacoes.solicitar_recomendacoes()
#     if resultado["status"] == "erro":
#         erro = resultado["mensagem"]
#     elif resultado["status"] == "sucesso":
#         habilidades = resultado["recomendacoes"]
#     return render_template("TelaRecomendacoesDoSistema.html", erro=erro, habilidades=habilidades)


@bp.route("/login", methods=["GET", "POST"])
def tela_login_usuario_controle():
    # erro = None
    # if request.method == "POST":
    #     resultado = controleLoginUsuario.realizar_login(request.form["email"], request.form["senha"])
    #     if resultado["status"] == "erro":
    #         erro = resultado["mensagem"]
    #     elif resultado["status"] == "sucesso":
    #         return redirect("/inicio")
    # return render_template(controleLoginUsuario.tela, erro=erro)
    return render_template("TelaLoginUsuario.html")
