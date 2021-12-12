from flask import Blueprint, request
import requests

bp = Blueprint("routes", __name__)

MAP_SERVICOS = {
    "servico-controle-acesso": {
        "domain": "localhost",
        "port": "5000",
    },
    "servico-habilidade": {
        "domain": "localhost",
        "port": "5001",
    },
    "servico-plano-desenvolvimento": {
        "domain": "localhost",
        "port": "5002",
    },
}

@bp.route("/<string:service>/<string:path>", methods=["POST", "GET"])
def mapeamento(service, path):
    func = getattr(requests, request.method.lower())

    domain = MAP_SERVICOS.get(service).get("domain")
    port = MAP_SERVICOS.get(service).get("port")
    url = f"http://{domain}:{port}/{path}"

    resposta = func(url, json=request.json)

    return resposta.json()
