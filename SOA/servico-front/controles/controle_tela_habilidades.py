from flask import session

from comunicacao.comunicacao_back import ComunicacaoBack


class ControleTelaHabilidades:
    def __init__(self):
        self.tela = "TelaHabilidades.html"
        self.comunicacao_back = ComunicacaoBack()

    def consultar_habilidades(self) -> dict:
        email = session.get("email_usuario")

        if not email:
            return {"erro": "Nenhum usuário logado"}

        return self.comunicacao_back.consultar_plano_de_desenvolvimento(email)
