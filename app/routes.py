from flask import Blueprint, render_template, redirect, request

from model.usuario.administrador.administrador import Administrador
from model.usuario.colaborador.colaborador import Colaborador
from model.usuario.cadastro_usuario import CadastroUsuario
from model.fachadas.fachada import Fachada
from controles.tela_login_usuario_controle import TelaLoginUsuarioControle

bp = Blueprint("routes", __name__)

@bp.route("/teste", methods=["GET"])
def teste():
    cadastro = CadastroUsuario()

    usuario = cadastro.consultar_usuario(email="ccal2@cin.ufpe.br")

    resultado = ""
    if usuario is not None:
        if type(usuario) is Administrador:
            resultado += f"(email: {usuario.email.email}, nome: {usuario.nome})"
        else:
            resultado += f"(email: {usuario.email.email}, nome: {usuario.nome}, area: {usuario.area}, cargo: {usuario.cargo}, interesse: ["
            for interesse in usuario.interesses:
                resultado += f"(titulo: {interesse.titulo}), "
            resultado += "])"

    return resultado


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
    controle = TelaLoginUsuarioControle()
    error = None
    if request.method == "POST":
        resultado = controle.realizar_login(request.form["email"], request.form["password"])
        if "erro" in resultado.keys():
            error = resultado["erro"]
        if "redirecionar" in resultado.keys():
            return redirect(resultado["redirecionar"])
    return render_template(controle.tela, error=error)
