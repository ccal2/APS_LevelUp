from model.controladores.fachada import Fachada
from model.usuario.colaborador.colaborador import Colaborador
from model.habilidade.habilidades import Habilidade


class TelaRecomendacoesDoSistemaControle:
    def __init__(self):
        self.fachada = Fachada()
        self.tela = "TelaRecomendacoesDoSistema.html"

    def solicitar_recomendacoes(self, colaborador: Colaborador) -> "list[Habilidade]":
        resultado_recomendacoes = self.fachada.solicitar_recomendacoes(colaborador)
        return resultado_recomendacoes
