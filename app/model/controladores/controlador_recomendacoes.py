from model.usuario.colaborador.colaborador import Colaborador
from model.habilidade.habilidades import Habilidade
from model.interesse.cadastro_interesse import CadastroInteresse
from model.habilidade.cadastro_habilidade import CadastroHabilidade


class ControladorRecomendacoes:
    def __init__(self, cadastro_interesse: CadastroInteresse = None, cadastro_habilidade: CadastroHabilidade = None):
        if cadastro_interesse is None:
            self.cadastro_interesse = CadastroInteresse()
        else:
            self.cadastro_interesse = cadastro_interesse

        if cadastro_habilidade is None:
            self.cadastro_habilidade = CadastroHabilidade()
        else:
            self.cadastro_habilidade = cadastro_habilidade

    def solicitar_recomendacoes(self, colaborador: Colaborador) -> "list[Habilidade]":
        interesses = self.cadastro_interesse.consultar_interesses(colaborador)
        habilidades = self.cadastro_habilidade.consultar_habilidades(interesses)

        return habilidades
