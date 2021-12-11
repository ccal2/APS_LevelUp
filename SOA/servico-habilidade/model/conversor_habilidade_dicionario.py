from model.habilidade import Habilidade


class ConversorHabilidadeDicionario:
    @staticmethod
    def habilidade_para_dicionario(habilidade: Habilidade):
        dicionario = {
            "nome": habilidade.nome,
            "descricao": habilidade.descricao,
            "nivel": habilidade.nivel,
            "interesses": habilidade.interesses,
        }

        return dicionario

    @staticmethod
    def dicionario_para_habilidade(dicionario) -> Habilidade:
        habilidade = Habilidade(
            nome=dicionario.get("nome"),
            descricao=dicionario.get("descricao"),
            nivel=dicionario.get("nivel"),
            interesses=dicionario.get("interesses"),
        )

        return habilidade
