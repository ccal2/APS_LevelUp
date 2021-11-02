from Usuario.Colaborador.Colaborador import Colaborador
from Interesse.Interesse import Interesse

class ColaboradorDicionarioConversor:

    @staticmethod
    def colaboradorParaDicionario(colaborador: Colaborador):
        ids_interesses = list(map(lambda x: x.titulo, colaborador.interesses))

        dicionario = {
            "email": colaborador.email,
            "nome": colaborador.nome,
            "area": colaborador.area,
            "cargo": colaborador.cargo,
            "interesses": ids_interesses
        }

        return dicionario

    @staticmethod
    def dicionarioParaColaborador(dicionario) -> Colaborador:
        interesses = list(map(lambda x: Interesse(titulo=x), dicionario.get('interesses')))

        colaborador = Colaborador(
            email = dicionario.get('email'),
            nome = dicionario.get('nome'),
            area = dicionario.get('area'),
            cargo = dicionario.get('cargo'),
            interesses = interesses
        )

        return colaborador
