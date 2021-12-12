from utils.singleton import SingletonMeta

from model.cadastro_plano_de_desenvolvimento import CadastroPlanoDeDesenvolvimento
from model.conversor_plano_de_desenvolvimento_dicionario import ConversorPlanoDeDesenvolvimentoDicionario

class Fachada(metaclass=SingletonMeta):
    def __init__(self):
        self.cadastro = CadastroPlanoDeDesenvolvimento()

    def obter_plano_de_desenvolvimento(self, email: str):
        plano = self.cadastro.consultar_plano_de_desenvolvimento(email)

        # TODO:
        # - Pegar habilidades a partir dos IDs de plano.estado_por_habilidade
        # - Transformar mapeamento em JSON para o retorno da função
        #   Formato do JSON: JSON de habilidade + um campo pro estado
        #   {[
        #       {
        #           "nome": <>,
        #           "descricao": <>,
        #           "nivel": <>,
        #           "interesses": [<>, <>, <>, ...],
        #           "estado": <>
        #       },
        #   ]}
        return ConversorPlanoDeDesenvolvimentoDicionario.plano_de_desenvolvimento_para_dicionario(plano)
