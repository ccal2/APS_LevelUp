from typing import Optional
from model.usuario.colaborador.colaborador import Colaborador

from SubsistemaComunicacaoAPILoginGoogle.i_subsistema_comunicacao_API_login_google import (
    ISubsistemaComunicacaoAPILoginGoogle,
)
from SubsistemaComunicacaoAPILoginGoogle.fachada_comunicacao_API_login_google import FachadaComunicacaoAPILoginGoogle
from model.usuario.cadastro_usuario import CadastroUsuario


class ControladorRecomendacoes:
    # def __init__(self):

    def solicitar_recomendacoes(self, colaborador: Colaborador):
      return [
        {
          "nome": "Habilidade 1",
          "descricao": "Descricao 1",
          "nivel": 21
        }
      ]