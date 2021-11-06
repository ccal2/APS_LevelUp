from model.usuario.administrador.administrador import Administrador
from utils.email import Email


class ConversorAdministradorDicionario:
    @staticmethod
    def administrador_para_dicionario(administrador: Administrador):
        dicionario = {"email": administrador.email.email, "nome": administrador.nome}

        return dicionario

    @staticmethod
    def dicionario_para_administrador(dicionario) -> Administrador:
        administrador = Administrador(email=Email(dicionario.get("email")), nome=dicionario.get("nome"))

        return administrador
