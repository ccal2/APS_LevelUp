from flask import Blueprint, render_template, redirect, request

from model.usuario.administrador.administrador import Administrador
from model.usuario.colaborador.colaborador import Colaborador
from model.usuario.cadastro_usuario import CadastroUsuario
from model.fachadas.fachada import Fachada

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


@bp.route("/testarLogin", methods=["GET"])
def testarLogin():
    fachada = Fachada()
    resultado_login = fachada.realizar_login(email="ccal2@cin.ufpe.br", senha="senha123")

    resultado = "Erro desconhecido"
    # se não for None, pode ser um erro, um Administrador ou um Colaborador
    if resultado_login is None:
        resultado = "Usuário não encontrado"
    elif type(resultado_login) is Administrador:
        resultado = f"(email: {resultado_login.email.email}, nome: {resultado_login.nome})"
    elif type(resultado_login) is Colaborador:
        resultado = f"(email: {resultado_login.email.email}, nome: {resultado_login.nome}, area: {resultado_login.area}, cargo: {resultado_login.cargo}, interesse: ["
        for interesse in resultado_login.interesses:
            resultado += f"(titulo: {interesse.titulo}), "
        resultado += "])"
    elif resultado_login.get("status") == "error":
        if resultado_login.get("message") == "INVALID_PASSWORD":
            resultado = "Senha inválida"
        elif resultado_login.get("message") == "EMAIL_NOT_FOUND":
            resultado = "Email não cadastrado"

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
    error = None
    if request.method == "POST":
        # logar com firebase
        # verificar o tipo de usuario pra saber pra qual pagina redirecionar
        return redirect("inicio/colaborador")
    return render_template("TelaLoginUsuario.html", error=error)
