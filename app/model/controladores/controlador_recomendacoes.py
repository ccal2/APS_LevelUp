from model.usuario.cadastro_usuario import CadastroUsuario
from model.habilidade.habilidades import Habilidade
from model.habilidade.cadastro_habilidade import CadastroHabilidade


class ControladorRecomendacoes:
    def __init__(self, cadastro_usuario: CadastroUsuario = None, cadastro_habilidade: CadastroHabilidade = None):
        if cadastro_usuario is None:
            self.cadastro_usuario = CadastroUsuario()
        else:
            self.cadastro_usuario = cadastro_usuario

        if cadastro_habilidade is None:
            self.cadastro_habilidade = CadastroHabilidade()
        else:
            self.cadastro_habilidade = cadastro_habilidade

    def solicitar_recomendacoes(self, email: str) -> "list[Habilidade]":
        colaborador = self.cadastro_usuario.consultar_usuario(email)
        habilidades = self.cadastro_habilidade.consultar_habilidades(colaborador.interesses)

        return habilidades
