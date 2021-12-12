import requests


class APIServicoHabilidade:
    def __init__(self) -> None:
        self.url_base = "http://gateway:8000/servico-habilidade"

    def consultar_habilidades_por_ids(self, ids: "list[str]"):
        URL_DO_REQUEST = self.url_base + "/habilidades"

        body = {"ids": ids}

        resultado = requests.post(URL_DO_REQUEST, json=body)
        resultado_json = resultado.json()

        return resultado_json.get("habilidades")
