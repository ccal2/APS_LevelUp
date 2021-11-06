from flask import Blueprint, render_template, redirect, request

from model.usuario.colaborador.colaborador import Colaborador
from model.usuario.cadastro_usuario import CadastroUsuario
from model.fachadas.fachada import Fachada
from controles.tela_login_usuario_controle import TelaLoginUsuarioControle

bp = Blueprint("routes", __name__)


@bp.route("/teste", methods=["GET"])
def teste():
    cadastro = CadastroUsuario()
    colaborador = cadastro.consultar_usuario(email="ccal2@cin.ufpe.br")

    fachada = Fachada()
    recomendacoes = fachada.solicitar_recomendacoes(colaborador)

    resultado = f"Recomendações para {colaborador.nome}: ["
    for habilidade in recomendacoes:
        resultado += f"(nome: {habilidade.nome}, descrição: {habilidade.descricao}, nível: {habilidade.nivel}), "
    resultado += "]"

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
    habilidades = [{"nome": "Habilidade 1", "descricao": "Descricao 1", "nivel": 21}]
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
