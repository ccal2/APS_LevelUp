from model.interesse.interesses import Interesse


class InteresseDicionarioConversor:
    @staticmethod
    def interesse_para_dicionario(interesse: Interesse):
        dicionario = {"titulo": interesse.titulo}

        return dicionario

    @staticmethod
    def dicionario_para_interesse(dicionario) -> Interesse:
        interesse = Interesse(titulo=dicionario.get("titulo"))

        return interesse
