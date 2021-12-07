from model.plano_de_desenvolvimento.plano_de_desenvolvimento import EstadoHabilidade, PlanoDeDesenvolvimento


class ConversorPlanoDeDesenvolvimentoDicionario:
    @staticmethod
    def plano_de_desenvolvimento_para_dicionario(plano_de_desenvolvimento: PlanoDeDesenvolvimento):
        dicionario = {}

        mapeamento = plano_de_desenvolvimento.estado_por_habilidade
        for estado_por_habilidade in mapeamento:
            dicionario[estado_por_habilidade] = mapeamento[estado_por_habilidade].value

        return dicionario

    @staticmethod
    def dicionario_para_plano_de_desenvolvimento(dicionario) -> PlanoDeDesenvolvimento:
        mapeamento = {}
        if dicionario is not None:
            for estado_por_habilidade in dicionario:
                mapeamento[estado_por_habilidade] = EstadoHabilidade(dicionario[estado_por_habilidade])

        plano_de_desenvolvimento = PlanoDeDesenvolvimento(estado_por_habilidade=mapeamento)

        return plano_de_desenvolvimento
