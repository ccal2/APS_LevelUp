from app import app
from flask import render_template

from model.Usuario.Colaborador.RepositorioColaboradorFirestore import RepositorioColaboradorFirestore
from model.Usuario.Colaborador.Colaborador import Colaborador
from model.Interesse.Interesse import Interesse

carolCIN = Colaborador(
    email = "ccal2@cin.ufpe.br",
    nome = "Carolina Lopes",
    area = "D&O",
    cargo = "Engenheiro de Software I",
    interesses = [Interesse(titulo="Swift")]
)

carolCESAR = Colaborador(
    email = "ccal@cesar.org.br",
    nome = "Carolina Lopes",
    area = "D&O",
    cargo = "Engenheiro de Software I"
)

@app.route("/inserir", methods=["GET"])
def inserir():
    repo = RepositorioColaboradorFirestore()

    repo.inserir(carolCIN)
    repo.inserir(carolCESAR)

    colaborador = repo.consultarColaborador(email=carolCIN.email)

    return colaborador.__str__()


@app.route("/consultar", methods=["GET"])
def consultar():
    repo = RepositorioColaboradorFirestore()

    colaborador = repo.consultarColaborador(email=carolCIN.email)

    return render_template('consultaColaborador.html', colaborador=colaborador)

@app.route("/atualizar", methods=["GET"])
def atualizar():
    repo = RepositorioColaboradorFirestore()

    carolCIN.interesses += [Interesse(titulo="Objective-C")]
    repo.atualizar(carolCIN)

    colaborador = repo.consultarColaborador(email=carolCIN.email)

    return colaborador.__str__()

@app.route("/remover", methods=["GET"])
def remover():
    repo = RepositorioColaboradorFirestore()

    repo.remover(carolCESAR)

    return "OK"
