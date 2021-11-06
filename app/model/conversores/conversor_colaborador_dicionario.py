from model.usuario.colaborador.colaborador import Colaborador
from model.interesse.interesses import Interesse
from utils.email import Email


class ConversorColaboradorDicionario:
    @staticmethod
    def colaborador_para_dicionario(colaborador: Colaborador):
        ids_interesses = list(map(lambda x: x.titulo, colaborador.interesses))

        dicionario = {
            "email": colaborador.email.email,
            "nome": colaborador.nome,
            "area": colaborador.area,
            "cargo": colaborador.cargo,
            "interesses": ids_interesses,
        }

        return dicionario

    @staticmethod
    def dicionario_para_colaborador(dicionario, interesses: "list[Interesse]") -> Colaborador:
        colaborador = Colaborador(
            email=Email(dicionario.get("email")),
            nome=dicionario.get("nome"),
            area=dicionario.get("area"),
            cargo=dicionario.get("cargo"),
            interesses=interesses,
        )

        return colaborador
