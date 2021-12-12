from flask import Blueprint, request
import requests

bp = Blueprint("routes", __name__)

MAP_SERVICOS = {
    "servico-controle-acesso": {
        "domain": "controle_acesso",
        "port": "5000",
    },
    "servico-habilidade": {
        "domain": "habilidade",
        "port": "5001",
    },
    "servico-plano-desenvolvimento": {
        "domain": "plano_desenvolvimento",
        "port": "5002",
    },
}

@bp.route("/<string:service>/<string:path>", methods=["POST", "GET"])
@bp.route("/<string:service>/<string:path>/<optional_parameter>", methods=["POST", "GET"])
def mapeamento(service, path, optional_parameter=None):
    func = getattr(requests, request.method.lower())

    domain = MAP_SERVICOS.get(service).get("domain")
    port = MAP_SERVICOS.get(service).get("port")
    url = f"http://{domain}:{port}/{path}"

    if optional_parameter is not None:
        url += "/" + optional_parameter

    resposta = func(url, json=request.json)

    return (resposta.json(), resposta.status_code)
