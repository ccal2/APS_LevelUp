from typing import Optional

from SubsistemaComunicacaoAPILoginGoogle.i_subsistema_comunicacao_API_login_google import (
    ISubsistemaComunicacaoAPILoginGoogle,
)
from SubsistemaComunicacaoAPILoginGoogle.fachada_comunicacao_API_login_google import FachadaComunicacaoAPILoginGoogle
from model.usuario.cadastro_usuario import CadastroUsuario


class ControladorLoginUsuario:
    def __init__(
        self, cadastro_usuario: CadastroUsuario = None, fachada_login: ISubsistemaComunicacaoAPILoginGoogle = None
    ):
        if cadastro_usuario is None:
            self.cadastro_usuario = CadastroUsuario()
        else:
            self.cadastro_usuario = cadastro_usuario

        if fachada_login is None:
            self.fachada_login = FachadaComunicacaoAPILoginGoogle()
        else:
            self.fachada_login = fachada_login

    def realizar_login(self, email: str, senha: str):  #  -> Optional[Usuario] | str
        resultado = self.fachada_login.login(email, senha)

        if resultado["status"] == "success":
            return self.cadastro_usuario.consultar_usuario(email)
        else:
            return resultado
