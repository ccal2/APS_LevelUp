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

@bp.route("/<service:service>/<path:path>", methods=["POST", "GET"])
def mapeamento(service, path):
    func = getattr(requests, request.args.get("method").toLower())

    domain = MAP_SERVICOS.get(service).get("url")
    port = MAP_SERVICOS.get(service).get("port")
    url = f"{domain}:{port}/{path}"

    return func(url, data=request.data)
