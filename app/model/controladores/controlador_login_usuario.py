from typing import Optional

from model.adaptadores.interface_login import InterfaceLogin
from model.usuario.cadastro_usuario import CadastroUsuario


class ControladorLoginUsuario:
    def __init__(self, servico_login: InterfaceLogin, cadastro_usuario: CadastroUsuario = None):
        self.servico_login = servico_login

        if cadastro_usuario is None:
            self.cadastro_usuario = CadastroUsuario()
        else:
            self.cadastro_usuario = cadastro_usuario

    def realizar_login(self, email: str, senha: str):
        return self.servico_login.realizar_login(email, senha)
