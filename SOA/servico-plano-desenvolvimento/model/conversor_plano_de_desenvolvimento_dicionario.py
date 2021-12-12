from model.plano_de_desenvolvimento import EstadoHabilidade, PlanoDeDesenvolvimento


class ConversorPlanoDeDesenvolvimentoDicionario:
    @staticmethod
    def plano_de_desenvolvimento_para_dicionario(plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        dicionario = {
            "colaborador": plano_de_desenvolvimento.id_colaborador
        }

        mapeamento = plano_de_desenvolvimento.estado_por_habilidade
        for estado_por_habilidade in mapeamento:
            dicionario[estado_por_habilidade] = mapeamento[estado_por_habilidade].value

        return dicionario

    @staticmethod
    def dicionario_para_plano_de_desenvolvimento(dicionario) -> PlanoDeDesenvolvimento:
        mapeamento = {}

        if dicionario is not None:
            mapeamento_estado_por_habilidade = dicionario.get("estado_por_habilidade")
            if mapeamento_estado_por_habilidade is not None:
                for estado_por_habilidade in mapeamento_estado_por_habilidade:
                    mapeamento[estado_por_habilidade] = EstadoHabilidade(mapeamento_estado_por_habilidade[estado_por_habilidade])

        id_colaborador = dicionario.get("colaborador")
        if id_colaborador is None:
            id_colaborador = ""

        plano_de_desenvolvimento = PlanoDeDesenvolvimento(id_colaborador, estado_por_habilidade=mapeamento)

        return plano_de_desenvolvimento
