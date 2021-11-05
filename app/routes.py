from flask import Blueprint, render_template, redirect, request

from model.usuario.colaborador.repositorio_colaborador_firestore import RepositorioColaboradorFirestore

bp = Blueprint("routes", __name__)


@bp.route("/consultar", methods=["GET"])
def consultar():
    repo = RepositorioColaboradorFirestore()

    colaborador = repo.consultar_colaborador(email="ccal2@cin.ufpe.br")

    return render_template("consulta_colaborador.html", colaborador=colaborador)


@bp.route("/inicio/colaborador", methods=["GET"])
def tela_inicio_colaborador_controle():
    return render_template("TelaInicioColaborador.html")


@bp.route("/inicio/administrador", methods=["GET"])
def tela_inicio_administrador_controle():
    return render_template("TelaInicioAdministrador.html")


@bp.route("/recomendacoes/colaborador", methods=["GET"])
def tela_recomendacoes_do_sistema_controle():
    # precisa chamar o metodo que vai pegar o usuario logado e gerar as recomendacoes
    # depois passar pro template
    return render_template("TelaRecomendacoesDoSistema.html")


@bp.route("/login", methods=["GET", "POST"])
def tela_login_usuario_controle():
    error = None
    if request.method == "POST":
        # logar com firebase
        # verificar o tipo de usuario pra saber pra qual pagina redirecionar
        return redirect("inicio/colaborador")
    return render_template("TelaLoginUsuario.html", error=error)
