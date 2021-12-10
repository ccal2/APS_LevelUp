from model.colaborador.colaborador import Colaborador
from utils.email import Email
from model.conversores.conversor_plano_de_desenvolvimento_dicionario import ConversorPlanoDeDesenvolvimentoDicionario


class ConversorColaboradorDicionario:
    @staticmethod
    def colaborador_para_dicionario(colaborador: Colaborador):
        dicionario = {
            "email": colaborador.email.email,
            "nome": colaborador.nome,
            "area": colaborador.area,
            "cargo": colaborador.cargo,
            "interesses": colaborador.interesses,
            "plano_de_desenvolvimento": ConversorPlanoDeDesenvolvimentoDicionario.plano_de_desenvolvimento_para_dicionario(
                colaborador.plano_de_desenvolvimento
            ),
        }

        return dicionario

    @staticmethod
    def dicionario_para_colaborador(dicionario) -> Colaborador:
        colaborador = Colaborador(
            email=Email(dicionario.get("email")),
            nome=dicionario.get("nome"),
            area=dicionario.get("area"),
            cargo=dicionario.get("cargo"),
            interesses=dicionario.get("interesses"),
            plano_de_desenvolvimento=ConversorPlanoDeDesenvolvimentoDicionario.dicionario_para_plano_de_desenvolvimento(
                dicionario.get("plano_de_desenvolvimento")
            ),
        )

        return colaborador
