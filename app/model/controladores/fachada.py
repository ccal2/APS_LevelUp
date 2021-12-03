from model.controladores.controlador_login_usuario import ControladorLoginUsuario
from model.controladores.controlador_recomendacoes import ControladorRecomendacoes
from model.adaptadores.adaptador_login_firebase import AdaptadorLoginFirebase
from model.usuario.colaborador.colaborador import Colaborador
from model.habilidade.habilidades import Habilidade


class Fachada:
    def __init__(self):
        self.controlador_login_usuario = ControladorLoginUsuario(servico_login=AdaptadorLoginFirebase())
        self.controlador_recomendacoes = ControladorRecomendacoes()

    def realizar_login(self, email: str, senha: str):
        return self.controlador_login_usuario.realizar_login(email, senha)

    def solicitar_recomendacoes(self, colaborador: Colaborador) -> "list[Habilidade]":
        return self.controlador_recomendacoes.solicitar_recomendacoes(colaborador)
