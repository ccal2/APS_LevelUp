from model.usuario.colaborador.colaborador import Colaborador
from utils.email import Email


class ConversorColaboradorDicionario:
    @staticmethod
    def colaborador_para_dicionario(colaborador: Colaborador):
        dicionario = {
            "email": colaborador.email.email,
            "nome": colaborador.nome,
            "area": colaborador.area,
            "cargo": colaborador.cargo,
            "interesses": colaborador.ids_interesses,
        }

        return dicionario

    @staticmethod
    def dicionario_para_colaborador(dicionario) -> Colaborador:
        colaborador = Colaborador(
            email=Email(dicionario.get("email")),
            nome=dicionario.get("nome"),
            area=dicionario.get("area"),
            cargo=dicionario.get("cargo"),
            ids_interesses=dicionario.get("interesses"),
        )

        return colaborador
