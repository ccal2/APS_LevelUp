from flask import session, request

from comunicacao.comunicacao_back import ComunicacaoBack


class ControleTelaLogin:
    def __init__(self):
        self.tela = "TelaHabilidades.html"
        self.comunicacao_back = ComunicacaoBack()

    def realizar_login(self) -> dict:
        # Verificar se form foi enviado
        if not request.form:
            return {
                "erro": "Body inváildo. Deve ter um form com \"email\" e \"senha\"."
            }

        # Verificar se o form contém email e senha
        email = request.form.get("email")
        senha = request.form.get("senha")
        if email is None or senha is None:
            return {
                "erro": "Body inváildo. O form deve ter os campos \"email\" e \"senha\"."
            }

        resultado = self.comunicacao_back.realizar_login(email, senha)

        if resultado.get("erro") is not None:
            session["email_usuario"] = email

        return resultado
