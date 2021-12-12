from flask import session

from comunicacao.comunicacao_back import ComunicacaoBack



class TelaHabilidadesControle:
    def __init__(self):
        self.tela = "TelaHabilidades.html"
        self.comunicacao_back = ComunicacaoBack()

    def consultar_habilidades(self) -> dict:
        # email = session.get("email_usuario")
        email = "ccal2@cin.ufpe.br"

        if not email:
            return {"erro": "Nenhum usuário logado"}

        return self.comunicacao_back.consultar_plano_de_desenvolvimento(email)
