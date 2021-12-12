from utils.singleton import SingletonMeta
from flask import request
from http import HTTPStatus

from model.cadastro_habilidade import CadastroHabilidade
from model.conversor_habilidade_dicionario import ConversorHabilidadeDicionario


class Fachada(metaclass=SingletonMeta):
    def __init__(self):
        self.cadastro = CadastroHabilidade()

    def consultar_habilidades(self):
        # Verificar se JSON foi enviado
        if not request.json:
            return (
                f'Body inváildo. Deve ter um JSON com array "interesses".',
                HTTPStatus.BAD_REQUEST,
            )

        # Verificar se a lista de interesses foi enviada no body da requisição
        interesses = request.json.get("interesses")
        if not interesses or type(interesses) is not list:
            return (
                f'Body inváildo. O JSON deve ter um campo "interesses" com um array não-vazio.',
                HTTPStatus.BAD_REQUEST,
            )

        habilidades = self.cadastro.consultar_habilidades_por_interesses(interesses)

        if len(habilidades) == 0:
            return (
                f'Nenhuma habilidade encontrada para os interesses {interesses}',
                HTTPStatus.NOT_FOUND,
            )

        return {
            "habilidades": list(
                map(lambda x: ConversorHabilidadeDicionario.habilidade_para_dicionario(x), habilidades)
            )
        }
