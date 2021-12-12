from utils.singleton import SingletonMeta
from flask import request
from http import HTTPStatus

from model.cadastro_habilidade import CadastroHabilidade


class Controlador(metaclass=SingletonMeta):
    def __init__(self):
        self.cadastro = CadastroHabilidade()

    def consultar_habilidades(self):
        # Verificar se JSON foi enviado
        if not request.json:
            return (
                {
                    "erro": "Body inváildo. Deve ter um JSON com parâmetros para o filtro."
                },
                HTTPStatus.BAD_REQUEST,
            )

        # Verificar se a lista de ids ou de interesses foi enviada no body da requisição
        if request.json.get("ids"):
            return self.consultar_habilidades_por_ids()
        elif request.json.get("interesses"):
            return self.consultar_habilidades_por_interesses()
        else:
            return (
                {
                    "erro": "Body inváildo. O JSON deve ter um campo \"ids\" ou um campo \"interesses\" com um array não-vazio."
                },
                HTTPStatus.BAD_REQUEST,
            )

    def consultar_habilidades_por_ids(self):
        ids = request.json.get("ids")
        if not ids or type(ids) is not list:
            return (
                {
                    "erro": "Body inváildo. O JSON deve ter um campo \"ids\" com um array não-vazio."
                },
                HTTPStatus.BAD_REQUEST,
            )

        habilidades = self.cadastro.consultar_habilidades_por_ids(ids)

        if len(habilidades) == 0:
            return (
                {
                    "erro": f"Nenhuma habilidade encontrada para os ids {ids}."
                },
                HTTPStatus.NOT_FOUND,
            )

        return {"habilidades": habilidades}

    def consultar_habilidades_por_interesses(self):
        interesses = request.json.get("interesses")
        if not interesses or type(interesses) is not list:
            return (
                {
                    "erro": "Body inváildo. O JSON deve ter um campo \"interesses\" com um array não-vazio."
                },
                HTTPStatus.BAD_REQUEST,
            )

        habilidades = self.cadastro.consultar_habilidades_por_interesses(interesses)

        if len(habilidades) == 0:
            return (
                {
                    "erro": f"Nenhuma habilidade encontrada para os interesses {interesses}."
                },
                HTTPStatus.NOT_FOUND,
            )

        return {"habilidades": habilidades}
