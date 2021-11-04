from model.habilidade.habilidade import Habilidade
from model.interesse.Interesse import Interesse


class HabilidadeDicionarioConversor:
    @staticmethod
    def habilidade_para_dicionario(habilidade: Habilidade):
        ids_interesses = list(map(lambda x: x.titulo, habilidade.interesses))

        dicionario = {
            "nome": habilidade.nome,
            "descricao": habilidade.descricao,
            "nivel": habilidade.nivel,
            "interesses": ids_interesses,
        }

        return dicionario

    @staticmethod
    def dicionario_para_habilidade(dicionario) -> Habilidade:
        # TODO: pegar Interesse do banco de dados
        interesses = list(map(lambda x: Interesse(titulo=x), dicionario.get("interesses")))

        habilidade = Habilidade(
            nome=dicionario.get("nome"),
            descricao=dicionario.get("descricao"),
            nivel=dicionario.get("nivel"),
            interesses=interesses,
        )

        return habilidade
