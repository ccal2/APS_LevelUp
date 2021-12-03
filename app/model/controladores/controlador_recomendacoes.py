from model.usuario.colaborador.colaborador import Colaborador
from model.habilidade.habilidades import Habilidade
from model.habilidade.cadastro_habilidade import CadastroHabilidade


class ControladorRecomendacoes:
    def __init__(self, cadastro_habilidade: CadastroHabilidade = None):
        if cadastro_habilidade is None:
            self.cadastro_habilidade = CadastroHabilidade()
        else:
            self.cadastro_habilidade = cadastro_habilidade

    def solicitar_recomendacoes(self, colaborador: Colaborador) -> "list[Habilidade]":
        habilidades = self.cadastro_habilidade.consultar_habilidades(colaborador.interesses)

        return habilidades
