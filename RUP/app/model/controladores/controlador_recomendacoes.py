from model.colaborador.cadastro_colaborador import CadastroColaborador
from model.habilidade.habilidades import Habilidade
from model.habilidade.cadastro_habilidade import CadastroHabilidade


class ControladorRecomendacoes:
    def __init__(
        self, cadastro_colaborador: CadastroColaborador = None, cadastro_habilidade: CadastroHabilidade = None
    ):
        if cadastro_colaborador is None:
            self.cadastro_colaborador = CadastroColaborador()
        else:
            self.cadastro_colaborador = cadastro_colaborador

        if cadastro_habilidade is None:
            self.cadastro_habilidade = CadastroHabilidade()
        else:
            self.cadastro_habilidade = cadastro_habilidade

    def solicitar_recomendacoes(self, email: str) -> "list[Habilidade]":
        colaborador = self.cadastro_colaborador.consultar_colaborador(email)
        habilidades = self.cadastro_habilidade.consultar_habilidades(colaborador.interesses)

        return habilidades
