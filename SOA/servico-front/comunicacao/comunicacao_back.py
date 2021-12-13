import requests

from utils.singleton import SingletonMeta


class ComunicacaoBack(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.url_gateway = "http://gateway:8000"
        self.url_servico_controle_acesso = self.url_gateway + "/servico-controle-acesso"
        self.url_servico_plano_desenvolvimento = self.url_gateway + "/servico-plano-desenvolvimento"
        self.url_servico_habilidade = self.url_gateway + "/servico-habilidade"

    def realizar_login(self, email: str, senha: str) -> dict:
        url = f"{self.url_servico_controle_acesso}/login"

        body = {
            "email": email,
            "senha": senha
        }

        resultado = requests.post(url, json=body)

        return resultado.json()

    def consultar_plano_de_desenvolvimento(self, id_colaborador: str) -> dict:
        url = f"{self.url_servico_plano_desenvolvimento}/plano-de-desenvolvimento/{id_colaborador}"

        resultado = requests.get(url)

        return resultado.json()
