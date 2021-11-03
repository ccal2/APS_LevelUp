from app import app
from flask import render_template

from model.usuario.colaborador.RepositorioColaboradorFirestore import RepositorioColaboradorFirestore


@app.route("/consultar", methods=["GET"])
def consultar():
    repo = RepositorioColaboradorFirestore()

    colaborador = repo.consultarColaborador(email="ccal2@cin.ufpe.br")

    return render_template("consultaColaborador.html", colaborador=colaborador)
