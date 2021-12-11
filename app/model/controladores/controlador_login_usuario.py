from typing import Optional

from model.adaptadores.interface_login import InterfaceLogin
from model.colaborador.cadastro_colaborador import CadastroColaborador


class ControladorLoginUsuario:
    def __init__(self, servico_login: InterfaceLogin, cadastro_colaborador: CadastroColaborador = None):
        self.servico_login = servico_login

        if cadastro_colaborador is None:
            self.cadastro_colaborador = CadastroColaborador()
        else:
            self.cadastro_colaborador = cadastro_colaborador

    def realizar_login(self, email: str, senha: str):
        return self.servico_login.realizar_login(email, senha)
