from model.controladores.fachada import Fachada
from model.usuario.administrador.administrador import Administrador
from model.usuario.colaborador.colaborador import Colaborador


class TelaLoginUsuarioControle:
    def __init__(self):
        self.fachada = Fachada()
        self.tela = "TelaLoginUsuario.html"

    def realizar_login(self, email, senha):
        return self.fachada.realizar_login(email=email, senha=senha)
