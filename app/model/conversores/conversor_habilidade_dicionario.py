from model.habilidade.habilidades import Habilidade


class ConversorHabilidadeDicionario:
    @staticmethod
    def habilidade_para_dicionario(habilidade: Habilidade):
        dicionario = {
            "nome": habilidade.nome,
            "descricao": habilidade.descricao,
            "nivel": habilidade.nivel,
            "interesses": habilidade.ids_interesses,
        }

        return dicionario

    @staticmethod
    def dicionario_para_habilidade(dicionario) -> Habilidade:
        habilidade = Habilidade(
            nome=dicionario.get("nome"),
            descricao=dicionario.get("descricao"),
            nivel=dicionario.get("nivel"),
            ids_interesses=dicionario.get("interesses"),
        )

        return habilidade
