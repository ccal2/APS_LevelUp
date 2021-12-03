from model.controladores.controlador_login_usuario import ControladorLoginUsuario
from model.controladores.controlador_recomendacoes import ControladorRecomendacoes
from model.usuario.colaborador.colaborador import Colaborador
from model.habilidade.habilidades import Habilidade


class Fachada:
    def __init__(self):
        self.controlador_login_usuario = ControladorLoginUsuario()
        self.controlador_recomendacoes = ControladorRecomendacoes()

    def realizar_login(self, email: str, senha: str):  #  -> Optional[Usuario] | str
        return self.controlador_login_usuario.realizar_login(email, senha)

    def solicitar_recomendacoes(self, colaborador: Colaborador) -> "list[Habilidade]":
        return self.controlador_recomendacoes.solicitar_recomendacoes(colaborador)
