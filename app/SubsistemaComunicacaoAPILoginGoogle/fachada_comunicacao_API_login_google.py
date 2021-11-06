from SubsistemaComunicacaoAPILoginGoogle.i_subsistema_comunicacao_API_login_google import (
    ISubsistemaComunicacaoAPILoginGoogle,
)
from SubsistemaComunicacaoAPILoginGoogle.controlador_login import ControladorLogin


class FachadaComunicacaoAPILoginGoogle(ISubsistemaComunicacaoAPILoginGoogle):
    def login(self, email: str, senha: str):
        controlador = ControladorLogin()
        return controlador.login(email, senha)
