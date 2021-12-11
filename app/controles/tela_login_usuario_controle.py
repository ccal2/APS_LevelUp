from flask import session

from model.controladores.fachada import Fachada


class TelaLoginUsuarioControle:
    def __init__(self):
        self.fachada = Fachada()
        self.tela = "TelaLoginUsuario.html"

    def realizar_login(self, email, senha):
        resultado = self.fachada.realizar_login(email=email, senha=senha)
        if resultado["status"] == "sucesso":
            session["email_usuario"] = email
        else:
            session["email_usuario"] = None

        return resultado
