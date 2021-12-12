import requests

from utils.singleton import SingletonMeta


class ComunicacaoBack(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.url_gateway = "http://gateway:8000"
        self.url_servico_controle_acesso = self.url_gateway + "/servico-controle-acesso"
        self.url_servico_plano_desenvolvimento = self.url_gateway + "/servico-plano-desenvolvimento"
        self.url_servico_habilidade = self.url_gateway + "/servico-habilidade"

    def consultar_plano_de_desenvolvimento(self, id_colaborador: str) -> dict:
        URL_DO_REQUEST = f"{self.url_servico_plano_desenvolvimento}/plano-de-desenvolvimento/{id_colaborador}"

        resultado = requests.get(URL_DO_REQUEST)

        return resultado.json()
