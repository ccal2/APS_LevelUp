from model.habilidade.habilidades import Habilidade
from model.interesse.interesses import Interesse


class ConversorHabilidadeDicionario:
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
    def dicionario_para_habilidade(dicionario, interesses: "list[Interesse]") -> Habilidade:
        habilidade = Habilidade(
            nome=dicionario.get("nome"),
            descricao=dicionario.get("descricao"),
            nivel=dicionario.get("nivel"),
            interesses=interesses,
        )

        return habilidade
