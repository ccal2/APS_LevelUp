from utils.singleton import SingletonMeta
from http import HTTPStatus

from model.cadastro_plano_de_desenvolvimento import CadastroPlanoDeDesenvolvimento
from model.api_servico_habilidade import APIServicoHabilidade


class Controlador(metaclass=SingletonMeta):
    def __init__(self):
        self.cadastro = CadastroPlanoDeDesenvolvimento()
        self.servico_habilidade = APIServicoHabilidade()

    def consultar_plano_de_desenvolvimento(self, id_colaborador: str):
        plano = self.cadastro.consultar_plano_de_desenvolvimento(id_colaborador)

        if plano is None:
            return (
                {
                    "erro": f"Nenhum plano de desenvolvimento encontrado para o colaborador com id {id_colaborador}"
                },
                HTTPStatus.NOT_FOUND,
            )

        mapeamento = plano.get("estado_por_habilidade")
        if mapeamento is None or len(mapeamento) == 0:
            return {"habilidades": []}

        ids_habilidades = list(mapeamento.keys())
        habilidades = self.servico_habilidade.consultar_habilidades_por_ids(ids_habilidades)

        for habilidade in habilidades:
            id_habilidade = habilidade.get("nome")
            if id_habilidade:
                habilidade["estado"] = mapeamento.get(id_habilidade, 0)

        return {"habilidades": habilidades}
