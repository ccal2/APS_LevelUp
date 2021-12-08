from flask import session

from model.controladores.fachada import Fachada
from model.habilidade.habilidades import Habilidade


class TelaRecomendacoesDoSistemaControle:
    def __init__(self):
        self.fachada = Fachada()
        self.tela = "TelaRecomendacoesDoSistema.html"

    def solicitar_recomendacoes(self) -> "list[Habilidade]":
        email = session.get("email_usuario")

        if not email:
            return {"status": "erro", "mensagem": "Nenhum usuário logado"}

        resultado_recomendacoes = self.fachada.solicitar_recomendacoes(email)

        return {"status": "sucesso", "recomendacoes": resultado_recomendacoes}
