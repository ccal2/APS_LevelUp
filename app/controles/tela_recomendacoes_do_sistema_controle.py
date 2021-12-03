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
            return {
                "status": "erro",
                "mensagem": "Nenhum usuário logado"
            }

        # TODO: tratar possíveis erros de solicitar_recomendacoes
        resultado_recomendacoes = self.fachada.solicitar_recomendacoes(email)

        return resultado_recomendacoes
