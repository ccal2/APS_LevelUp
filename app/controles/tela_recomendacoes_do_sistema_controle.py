from model.fachadas.fachada import Fachada
from model.usuario.colaborador.colaborador import Colaborador

class TelaRecomendacoesDoSistemaControle:
    def __init__(self):
        self.fachada = Fachada()
        self.tela = "TelaRecomendacoesDoSistema.html"

    def solicitar_recomendacoes(self, colaborador: Colaborador):
      resultado_recomendacoes = self.fachada.solicitar_recomendacoes(colaborador)
      
      